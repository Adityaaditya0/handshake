# 🖱️ Virtual Mouse using MediaPipe & OpenCV

A **hand-gesture controlled virtual mouse** built using **MediaPipe**, **OpenCV**, and **PyAutoGUI**.  
Move your hand to move the cursor, and perform a **pinch gesture (Index + Thumb)** to click—completely touchless.

---

## 🚀 Features

- Control mouse with hand gestures  
- Cursor moves based on index fingertip  
- Pinch gesture → Left click  
- Real-time hand tracking  
- Smooth cursor movement  
- Works on laptop webcam or USB camera  

---

## 📸 Demo (Concept)

> Move your index finger → cursor moves  
> Bring thumb & index together → left click  

---

## 🧰 Tech Stack

- Python 3.8–3.12  
- OpenCV  
- MediaPipe  
- PyAutoGUI  
- NumPy  

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
pip install mediapipe==0.10.9
pip install opencv-python
pip install pyautogui
pip install numpy
python virtual_mouse.py
