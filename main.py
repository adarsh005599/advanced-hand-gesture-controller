import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pyautogui
import urllib.request
import os
import math

# We map the hand skeleton manually to avoid using the deleted 'solutions.drawing_utils'
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),        # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),        # Index finger
    (5, 9), (9, 10), (10, 11), (11, 12),   # Middle finger
    (9, 13), (13, 14), (14, 15), (15, 16), # Ring finger
    (13, 17), (0, 17), (17, 18), (18, 19), (19, 20) # Pinky
]

def download_model():
    """Automatically downloads the required MediaPipe Task model if missing."""
    model_path = 'hand_landmarker.task'
    url = 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task'
    if not os.path.exists(model_path):
        print(f"Downloading MediaPipe AI model... please wait.")
        urllib.request.urlretrieve(url, model_path)
    return model_path

def main():
    model_path = download_model()

    base_options = python.BaseOptions(model_asset_path=model_path)
    # Changed num_hands to 1 so the system doesn't get confused if it sees both hands
    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        num_hands=1, 
        min_hand_detection_confidence=0.7,
        min_hand_presence_confidence=0.7,
        min_tracking_confidence=0.7
    )
    
    detector = vision.HandLandmarker.create_from_options(options)
    cap = cv2.VideoCapture(0)

    # Key states and toggle switches to prevent spamming
    left_pressed = False
    right_pressed = False
    three_finger_active = False
    pinch_active = False

    print("Advanced Controller Started! Press 'q' in the video window to quit.")

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Mirror image for a natural selfie-view
        frame = cv2.flip(frame, 1)
        h, w, c = frame.shape

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        detection_result = detector.detect(mp_image)
        
        # Default UI Text
        current_gesture_text = "NO GESTURE"
        text_color = (255, 255, 0) # Yellow

        if detection_result.hand_landmarks:
            # Only process the first detected hand
            hand_landmarks = detection_result.hand_landmarks[0]
            
            # --- 1. DRAW SKELETON ---
            landmark_px = []
            for lm in hand_landmarks:
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_px.append((cx, cy))
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
            
            for connection in HAND_CONNECTIONS:
                start_idx, end_idx = connection
                cv2.line(frame, landmark_px[start_idx], landmark_px[end_idx], (0, 255, 0), 2)

            # --- 2. ANALYZE HAND DATA ---
            # Calculate distance between Thumb Tip (4) and Index Tip (8) for Pinching
            thumb_tip = hand_landmarks[4]
            index_tip = hand_landmarks[8]
            pinch_dist = math.hypot(index_tip.x - thumb_tip.x, index_tip.y - thumb_tip.y)

            # Count how many main fingers are UP (checking if tip is higher than the lower joint)
            fingers_up = 0
            if hand_landmarks[8].y < hand_landmarks[6].y: fingers_up += 1   # Index
            if hand_landmarks[12].y < hand_landmarks[10].y: fingers_up += 1 # Middle
            if hand_landmarks[16].y < hand_landmarks[14].y: fingers_up += 1 # Ring
            if hand_landmarks[20].y < hand_landmarks[18].y: fingers_up += 1 # Pinky

            # --- 3. EXECUTE GESTURES ---
            
            # Priority A: Is the user pinching?
            if pinch_dist < 0.05:
                current_gesture_text = "PINCH -> Spacebar"
                text_color = (0, 255, 255) # Cyan
                
                # Press space only ONCE per pinch
                if not pinch_active:
                    pyautogui.press('space')
                    pinch_active = True
                    
            # Priority B: Count the fingers
            else:
                pinch_active = False # Reset pinch so it can be used again

                if fingers_up == 0:
                    current_gesture_text = "FIST -> Left Arrow"
                    text_color = (0, 0, 255) # Red
                    if not left_pressed:
                        pyautogui.keyDown('left')
                        left_pressed = True

                elif fingers_up == 4:
                    current_gesture_text = "PALM -> Right Arrow"
                    text_color = (0, 255, 0) # Green
                    if not right_pressed:
                        pyautogui.keyDown('right')
                        right_pressed = True

                elif fingers_up == 1:
                    current_gesture_text = "1 FINGER -> Scroll UP"
                    text_color = (255, 100, 100) # Light Blue
                    pyautogui.scroll(50) # Scroll continuously while held

                elif fingers_up == 2:
                    current_gesture_text = "2 FINGERS -> Scroll DOWN"
                    text_color = (100, 255, 100) # Light Green
                    pyautogui.scroll(-50) # Scroll continuously while held

                elif fingers_up == 3:
                    current_gesture_text = "3 FINGERS -> Switch Window"
                    text_color = (255, 165, 0) # Orange
                    # Only trigger Alt+Tab ONCE per gesture
                    if not three_finger_active:
                        pyautogui.hotkey('alt', 'tab')
                        three_finger_active = True

            # --- 4. SAFETY RESETS ---
            # If 3 fingers are no longer held, reset the Alt-Tab trigger
            if fingers_up != 3:
                three_finger_active = False

            # If not Palm, release Right Arrow
            if fingers_up != 4 and right_pressed:
                pyautogui.keyUp('right')
                right_pressed = False
                
            # If not Fist, release Left Arrow
            if fingers_up != 0 and left_pressed:
                pyautogui.keyUp('left')
                left_pressed = False

        else:
            # NO HAND DETECTED: Release all keys instantly
            if left_pressed:
                pyautogui.keyUp('left')
                left_pressed = False
            if right_pressed:
                pyautogui.keyUp('right')
                right_pressed = False
            pinch_active = False
            three_finger_active = False

        # Show the video feed with text
        cv2.putText(frame, current_gesture_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
        cv2.imshow("Hand Detection Controller", frame)

        # Quit gracefully when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Final safety release when program closes
    if left_pressed: pyautogui.keyUp('left')
    if right_pressed: pyautogui.keyUp('right')

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()