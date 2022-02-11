import cv2
import numpy as np

# cap = cv2.VideoCapture(r"rolling_can.mov")
cap = cv2.VideoCapture("/Users/local/PycharmProjects/rollingcan_kennethlin/rolling_can.mov")

totalFrames = 0
countedFrames = 0
font = cv2.FONT_HERSHEY_SIMPLEX


while cap.isOpened():
    ret, frame = cap.read()
    totalFrames += 1
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        gray_blurred = cv2.GaussianBlur(gray, (11, 11), 0)
        detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=1, maxRadius=40)

        if detected_circles is not None:

            detected_circles = np.uint16(np.around(detected_circles))

            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                cv2.circle(frame, (a, b), r, (0, 255, 0), 2)
                cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

            countedFrames += 1

        cv2.putText(frame, 'total frames: ' + str(totalFrames), (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
        cv2.putText(frame, 'counted frames: ' + str(countedFrames), (50, 25), font, 1, (0, 255, 255), 2, cv2.LINE_4)

        cv2.imshow("Detected Circles", frame)
        k = cv2.waitKey(1) & 0xff
    else:
        break

cv2.waitKey(0)

cv2.destroyAllWindows()
cap.release()
