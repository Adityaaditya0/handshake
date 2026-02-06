import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Webcam Size
cam_w, cam_h = 640, 480

# Screen Size
screen_w, screen_h = pyautogui.size()

# MediaPipe Setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)
cap.set(3, cam_w)
cap.set(4, cam_h)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Draw landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get Index Finger Tip (landmark 8)
            x_index = int(hand_landmarks.landmark[8].x * cam_w)
            y_index = int(hand_landmarks.landmark[8].y * cam_h)

            # Get Thumb Tip (landmark 4)
            x_thumb = int(hand_landmarks.landmark[4].x * cam_w)
            y_thumb = int(hand_landmarks.landmark[4].y * cam_h)

            # Convert coordinates to screen space
            screen_x = np.interp(x_index, (0, cam_w), (0, screen_w))
            screen_y = np.interp(y_index, (0, cam_h), (0, screen_h))

            # Move Mouse
            pyautogui.moveTo(screen_x, screen_y, duration=0)

            # Calculate distance for click
            dist = np.hypot(x_thumb - x_index, y_thumb - y_index)

            # If fingers close → Click
            if dist < 40:
                cv2.circle(frame, (x_index, y_index), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()
                pyautogui.sleep(0.2)

            # Draw fingertip
            cv2.circle(frame, (x_index, y_index), 10, (255, 0, 0), cv2.FILLED)

    cv2.imshow("Virtual Mouse - MediaPipe", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
