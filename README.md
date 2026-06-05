# ✋ Hand Gesture Controller using OpenCV & MediaPipe
Control keyboard inputs using hand gestures in real time using Python, OpenCV, MediaPipe, and PyAutoGUI.

## Overview
This project detects hand gestures from a webcam feed and converts them into keyboard actions.

### Gesture Mapping
| Gesture | Action |
|----------|----------|
| 🖐️ Open Palm | Right Arrow Key |
| 👊 Fist | Left Arrow Key |

## Features

- Real-time hand tracking
- MediaPipe hand landmark detection
- Open Palm recognition
- Fist recognition
- Keyboard automation using PyAutoGUI
- Landmark visualization

## Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## Gesture Examples
### Open Palm → Right Arrow Key
<img width="634" height="520" alt="Screenshot 2026-06-05 211730" src="https://github.com/user-attachments/assets/2c9fa8cd-4822-4242-b95a-0c6a27f5af5a" />
<img width="4608" height="2080" alt="hg" src="https://github.com/user-attachments/assets/6fb4944a-4eb4-475e-a77b-6f23568aa876" />

### Fist → Left Arrow Key
<img width="641" height="515" alt="Screenshot 2026-06-05 211753" src="https://github.com/user-attachments/assets/498836c0-96a5-4440-94c3-343a3be4acad" />
<img width="4608" height="2080" alt="hg3" src="https://github.com/user-attachments/assets/17ef7276-b029-4b42-8621-f98065c10065" />


## How It Works
1. Webcam captures live video.
2. MediaPipe detects 21 hand landmarks.
3. Finger positions are analyzed.
4. Open Palm gesture triggers the Right Arrow key.
5. Fist gesture triggers the Left Arrow key.
6. Keys are released when no gesture is detected.

## Installation

Clone the repository:

```bash
git clone https://github.com/BhavyaShah2005/hand-gesture-controller.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```
## Skills Demonstrated

- Computer Vision
- Gesture Recognition
- Real-Time Video Processing
- Human Computer Interaction (HCI)
- Python Automation

## Future Improvements

- Additional gestures
- Volume control
- Mouse control
- Presentation controller
- Custom gesture mapping

## Author
Bhavya Shah

GitHub:
https://github.com/BhavyaShah2005
