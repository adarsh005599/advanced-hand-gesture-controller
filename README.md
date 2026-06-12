# 🖐️ Advanced Hand Gesture Controller

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge\&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Automation-red?style=for-the-badge)

**Control your computer hands-free using real-time hand gestures.**

Turn your webcam into a powerful gesture-recognition controller capable of scrolling, switching applications, navigating interfaces, and triggering keyboard actions without touching your keyboard.

</div>

---

## 🎥 Demo

> # Coming Soon

```text
demo.gif
```

A real-time AI-powered gesture control system that tracks your hand using MediaPipe's machine learning model and translates gestures into keyboard inputs and system actions.

---

# 🚀 Overview

Traditional keyboard shortcuts require physical interaction.

This project removes that dependency by transforming your hand into an intelligent controller.

Using Computer Vision and Machine Learning, the application tracks **21 hand landmarks** in real time and determines the exact state of each finger. Different finger combinations trigger specific keyboard commands and system automations.

Whether you're browsing the web, presenting slides, watching videos, or gaming, your hand becomes the controller.

---

# ✨ Features

✅ Real-Time Hand Tracking

✅ Dynamic Hand Skeleton Visualization

✅ Gesture-Based Keyboard Controls

✅ Continuous Scrolling Support

✅ Smart Input Debouncing

✅ One-Time Gesture Triggers

✅ Automatic AI Model Download

✅ Low-Latency Performance

✅ Cross-Platform Python Implementation

---

# 🎮 Gesture Controls

| Gesture          | Action        | Keyboard/System Command | Use Case                      |
| ---------------- | ------------- | ----------------------- | ----------------------------- |
| 👊 Fist          | Move Left     | Hold Left Arrow Key     | Racing Games, Menus           |
| 🖐️ Open Palm    | Move Right    | Hold Right Arrow Key    | Presentations, Navigation     |
| ☝️ Index Finger  | Scroll Up     | Continuous Scroll Up    | Articles, Websites            |
| ✌️ Peace Sign    | Scroll Down   | Continuous Scroll Down  | Long Documents                |
| 🤟 Three Fingers | Switch Window | Alt + Tab               | Multitasking                  |
| 🤏 Pinch Gesture | Spacebar      | Press Space             | YouTube, Media Players, Games |

---

# 🧠 How It Works

### 1️⃣ Webcam Capture

OpenCV continuously captures video frames from your webcam.

### 2️⃣ Hand Detection

MediaPipe's Hand Landmarker identifies:

* Hand presence
* Finger positions
* Joint coordinates
* Hand orientation

### 3️⃣ Gesture Recognition

The application analyzes:

* Finger states
* Relative landmark positions
* Pinch distances
* Hand direction

to determine which gesture is being performed.

### 4️⃣ Action Execution

PyAutoGUI converts detected gestures into:

* Keyboard presses
* Key holds
* Scroll events
* Application switching commands

---

# 🎯 Gesture Mapping Logic

### Finger Counting

The system determines whether each finger is:

```text
UP
or
DOWN
```

Then calculates the total number of visible fingers.

Examples:

```text
0 Fingers  → Fist
1 Finger   → Scroll Up
2 Fingers  → Scroll Down
3 Fingers  → Alt + Tab
4 Fingers  → Right Arrow
```

---

### Pinch Detection

The distance between:

```text
Thumb Tip
and
Index Finger Tip
```

is continuously measured.

When the distance falls below a threshold:

```text
Distance < Threshold
```

the application triggers:

```text
Spacebar Press
```

---

# 📂 Project Structure

```bash
advanced-hand-gesture-controller/
│
├── main.py
├── hand_landmarker.task
├── requirements.txt
├── README.md
│
└── assets/
    ├── demo.gif
    └── screenshots/
```

---

# 🛠️ Built With

### Python 3.12

Core programming language.

### OpenCV

* Webcam access
* Frame processing
* Visual rendering

### MediaPipe Tasks

* Real-time hand landmark detection
* Machine learning inference
* Gesture tracking

### PyAutoGUI

* Keyboard automation
* Scrolling
* Shortcut execution

---

# 📋 System Requirements

| Requirement | Version                 |
| ----------- | ----------------------- |
| Python      | 3.12                    |
| Webcam      | Required                |
| RAM         | 4 GB+ Recommended       |
| OS          | Windows / Linux / macOS |

---

# ⚠️ Important Compatibility Note

MediaPipe currently has compatibility issues with:

```text
Python 3.13 (Windows)
```

Using Python 3.13 may result in:

```python
AttributeError:
function 'free' not found
```

### Recommended Version

```bash
Python 3.12
```

---

# 🔧 Installation

## 1. Clone Repository

```bash
git clone https://github.com/adarsh005599/advanced-hand-gesture-controller.git

cd advanced-hand-gesture-controller
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

Or:

```bash
pip install -r requirements.txt
```

---

## 4. Run Application

```bash
python main.py
```

---

# 🎮 Usage

### Start the Application

Run:

```bash
python main.py
```

A window named:

```text
Hand Detection Controller
```

will appear.

---

### Using Gestures

1. Ensure your hand is visible.
2. Keep fingers within the camera frame.
3. Perform supported gestures.
4. Watch actions execute instantly.

---

### Quit Safely

Press:

```text
Q
```

while the camera window is focused.

This will:

* Stop webcam capture
* Release resources
* Terminate active key holds
* Exit cleanly

---

# 🔒 Smart Input Protection

To prevent accidental key spam, the application uses:

### Debouncing

Prevents rapid repeated firing of:

```text
Alt + Tab
```

and

```text
Spacebar
```

---

### State Tracking

The controller remembers:

```text
Current Gesture
Previous Gesture
```

ensuring commands only execute when intended.

---

# 🧠 Skills Demonstrated

### Computer Vision

* Image Processing
* Landmark Detection
* Real-Time Video Analysis

### Machine Learning Integration

* MediaPipe Tasks
* On-device Inference

### Human Computer Interaction (HCI)

* Gesture-Based Interfaces
* Alternative Input Systems

### Automation Engineering

* Keyboard Simulation
* System Shortcuts
* Event Handling

### Geometry & Mathematics

* Distance Calculations
* Coordinate Systems
* Landmark Mapping

---

# 🚀 Future Improvements

### 🎚️ Volume Control

Thumbs Up 👍

```text
Increase Volume
```

Thumbs Down 👎

```text
Decrease Volume
```

---

### 🖱️ Virtual Mouse

Control the cursor using:

```text
Index Finger Tracking
```

---

### ⚙️ Custom Configuration Panel

Allow users to:

* Remap gestures
* Change shortcuts
* Adjust sensitivity
* Create macros

---

### 🎮 Gaming Mode

Dedicated profile for:

* Racing games
* Platformers
* Simulators

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

### Adarsh Singh

Full Stack Developer • AI Enthusiast • Computer Vision Explorer

GitHub:

https://github.com/adarsh005599

---

<div align="center">

⭐ If you found this project useful, consider giving it a star.

Built with ❤️ using Python, OpenCV, MediaPipe, and PyAutoGUI.

</div>
