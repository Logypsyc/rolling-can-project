import cv2
import numpy as np

cap = cv2.VideoCapture("/Users/local/PycharmProjects/rollingcan_kennethlin/rolling_can.mov")

totalFrames = 0
countedFrames = 0
font = cv2.FONT_HERSHEY_SIMPLEX

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
result = cv2.VideoWriter('output.MOV', fourcc, 30, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    totalFrames += 1
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        gray_blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 100000000000000, param1=80, param2=10, minRadius=20, maxRadius=24)

        if detected_circles is not None:

            detected_circles = np.uint16(np.around(detected_circles))

            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
                cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

            countedFrames += 1

        cv2.putText(frame, 'total frames: ' + str(totalFrames), (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_4)
        cv2.putText(frame, 'counted frames: ' + str(countedFrames), (50, 25), font, 1, (0, 255, 0), 2, cv2.LINE_4)

        result.write(frame)
        cv2.imshow("Detected Circles", frame)

        k = cv2.waitKey(33) & 0xff
    else:
        break

cv2.waitKey(0)

cap.release()
result.release()
cv2.destroyAllWindows()
