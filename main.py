import cv2
import numpy as np

video = cv2.VideoCapture("/Users/local/PycharmProjects/rollingcan_kennethlin/IMG_9653.mov")

while video.isOpened():
    frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            cv2.circle(frame, (x, y), 5, (0, 128, 255), -1)
        cv2.imshow("frame", frame)