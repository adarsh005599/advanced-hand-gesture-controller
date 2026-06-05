import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Create hand detector
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Start webcam
cap = cv2.VideoCapture(0)

# Key states
left_pressed = False
right_pressed = False

while True:

    success, frame = cap.read()

    if not success:
        break

    # Mirror image
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_frame)

    gesture_detected = False

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # Draw hand skeleton
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand_landmarks.landmark

            # PALM
            if (
                landmarks[8].y < landmarks[6].y and
                landmarks[12].y < landmarks[10].y and
                landmarks[16].y < landmarks[14].y and
                landmarks[20].y < landmarks[18].y
            ):

                gesture_detected = True

                cv2.putText(
                    frame,
                    "PALM",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                if not right_pressed:
                    pyautogui.keyDown('right')
                    right_pressed = True

                if left_pressed:
                    pyautogui.keyUp('left')
                    left_pressed = False

            # FIST
            elif (
                landmarks[8].y > landmarks[6].y and
                landmarks[12].y > landmarks[10].y and
                landmarks[16].y > landmarks[14].y and
                landmarks[20].y > landmarks[18].y
            ):

                gesture_detected = True

                cv2.putText(
                    frame,
                    "FIST",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

                if not left_pressed:
                    pyautogui.keyDown('left')
                    left_pressed = True

                if right_pressed:
                    pyautogui.keyUp('right')
                    right_pressed = False

            # Draw landmarks
            for id, lm in enumerate(landmarks):

                h, w, c = frame.shape

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                cv2.circle(
                    frame,
                    (cx, cy),
                    5,
                    (0, 255, 0),
                    cv2.FILLED
                )

                cv2.putText(
                    frame,
                    str(id),
                    (cx, cy),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 0, 0),
                    1
                )

    # Release keys if no gesture detected
    if not gesture_detected:

        if left_pressed:
            pyautogui.keyUp('left')
            left_pressed = False

        if right_pressed:
            pyautogui.keyUp('right')
            right_pressed = False

    # Show webcam
    cv2.imshow("Hand Detection", frame)

    # Quit with q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Safety release
pyautogui.keyUp('left')
pyautogui.keyUp('right')

cap.release()
cv2.destroyAllWindows()




# import cv2
# import mediapipe as mp
# import pydirectinput

# # Initialize MediaPipe
# mp_hands = mp.solutions.hands
# mp_draw = mp.solutions.drawing_utils

# # Create hand detector
# hands = mp_hands.Hands(
#     static_image_mode=False,
#     max_num_hands=1,
#     min_detection_confidence=0.6,
#     min_tracking_confidence=0.6
# )

# # Start webcam
# cap = cv2.VideoCapture(0)

# left_pressed = False
# right_pressed = False

# while True:

#     success, frame = cap.read()

#     if not success:
#         continue

#     frame = cv2.flip(frame, 1)

#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     results = hands.process(rgb)

#     gesture_detected = False

#     if results.multi_hand_landmarks:

#         hand_landmarks = results.multi_hand_landmarks[0]
#         landmarks = hand_landmarks.landmark

#         # PALM
#         if (
#             landmarks[8].y < landmarks[6].y and
#             landmarks[12].y < landmarks[10].y and
#             landmarks[16].y < landmarks[14].y and
#             landmarks[20].y < landmarks[18].y
#         ):

#             gesture_detected = True

#             if not right_pressed:
#                 pydirectinput.keyDown('right')
#                 right_pressed = True

#             if left_pressed:
#                 pydirectinput.keyUp('left')
#                 left_pressed = False

#         # FIST
#         elif (
#             landmarks[8].y > landmarks[6].y and
#             landmarks[12].y > landmarks[10].y and
#             landmarks[16].y > landmarks[14].y and
#             landmarks[20].y > landmarks[18].y
#         ):

#             gesture_detected = True

#             if not left_pressed:
#                 pydirectinput.keyDown('left')
#                 left_pressed = True

#             if right_pressed:
#                 pydirectinput.keyUp('right')
#                 right_pressed = False

#     # No gesture -> release all keys
#     if not gesture_detected:

#         if left_pressed:
#             pydirectinput.keyUp('left')
#             left_pressed = False

#         if right_pressed:
#             pydirectinput.keyUp('right')
#             right_pressed = False

# # Safety release if program exits
# pydirectinput.keyUp('left')
# pydirectinput.keyUp('right')

# cap.release()
# cv2.destroyAllWindows()