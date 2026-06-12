# ✋ Advanced Hand Gesture Controller

Control your computer hands-free using real-time hand gestures. This project uses your webcam to track finger landmarks and translate them into keyboard inputs and system automations like scrolling or switching windows.

---

## 🚀 Overview

This application leverages computer vision to turn your hand into an interactive macro controller. By tracking 21 unique points on your hand, it reads the exact state of your fingers to execute precise combinations of system keys without any physical keyboard contact.

### 🎮 Gesture & Action Mapping

| Gesture | Visual Indicator | Keyboard / System Action | Best Used For |
| :--- | :--- | :--- | :--- |
| 👊 **Fist** (0 Fingers Up) | `FIST (<- LEFT)` | Holds down **Left Arrow** key | Racing games, navigating menus backward |
| 🖐️ **Open Palm** (4 Fingers Up) | `PALM (RIGHT ->)` | Holds down **Right Arrow** key | Racing games, moving to next slide |
| ☝️ **1 Finger Up** (Index) | `1 FINGER -> Scroll UP` | Continuous **Scroll Up** | Reading articles, scrolling feeds |
| ✌️ **2 Fingers Up** (Peace) | `2 FINGERS -> Scroll DOWN` | Continuous **Scroll Down** | Reading long documents, web browsing |
| 🤟 **3 Fingers Up** | `3 FINGERS -> Switch Window` | Fires **`Alt + Tab`** (Once) | Quick multitasking and window swapping |
| 🤏 **Pinch** (Thumb + Index) | `PINCH -> Spacebar` | Presses **Spacebar** (Once) | Pausing/Playing YouTube, jumping in games |

---

## ✨ Features

- **Real-Time Hand Tracking:** Ultra-low latency tracking using the modern MediaPipe Tasks vision engine.
- **Dynamic Joint Visualization:** Automatically draws an interactive green skeleton mapping over your hand joints.
- **Smart Input Throttling:** Built-in toggle switches prevent key spamming, ensuring events like `Alt + Tab` or `Spacebar` only fire exactly once per gesture.
- **Self-Healing Setup:** Automatically downloads the required machine learning model file (`hand_landmarker.task`) locally if it is missing from your directory.

---

## 🛠️ Built With

- **Python** (Recommended version: `3.12`)
- **OpenCV** (Real-time video capture & UI frame drawing)
- **MediaPipe Tasks** (On-device machine learning hand framework)
- **PyAutoGUI** (Cross-platform programmatic keyboard/mouse simulation)

---

## 📋 System Requirements & Prerequisites

> [!IMPORTANT]
> **Python Version Compatibility:** This project requires **Python 3.12**. MediaPipe's underlying native C++ bindings are currently incompatible with Python 3.13 on Windows platforms, which will throw an `AttributeError: function 'free' not found` runtime exception.

---

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/BhavyaShah2005/hand-gesture-controller.git](https://github.com/BhavyaShah2005/hand-gesture-controller.git)
cd hand-gesture-controller