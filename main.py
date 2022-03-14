import cv2 as cv
import numpy as np
import math

src = cv.imread(r"IMG_9905.jpeg", cv.IMREAD_GRAYSCALE)
dst = cv.Canny(src, 50, 200, None, 3)

# Copy edges to the images that will display the results in BGR
cdstP = cv.cvtColor(src, cv.COLOR_GRAY2BGR)
gray_blurred = cv.blur(cdstP, (5, 5))
linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 5, None, 0, 10000)

if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(gray_blurred, (l[0], l[1]), (l[2], l[3]), (0, 255, 0), 3, cv.LINE_AA)

x1 = linesP[0][0][0]
y1 = linesP[0][0][1]
x2 = linesP[0][0][2]
y2 = linesP[0][0][3]

x3 = linesP[1][0][0]
y3 = linesP[1][0][1]
x4 = linesP[1][0][2]
y4 = linesP[1][0][3]

points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
arrowedImage = cv.arrowedLine(gray_blurred, points[0], points[1], (0, 0, 255), 9)
arrowedImage = cv.arrowedLine(gray_blurred, points[3], points[2], (0, 0, 255), 9)

bottomPointX = int((x1 + x2)/2)
bottomPointY = int((y1 + y2)/2)
cv.imshow("Detected Lines - probabilistic hough transform", arrowedImage)
cv.waitKey()
