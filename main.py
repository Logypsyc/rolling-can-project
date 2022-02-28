import cv2
import numpy as np

img = cv2.imread("/Users/local/PycharmProjects/findcircles_kennethlin/test_l3.jpg")
# img = cv2.imread(r"C:\Users\klin1\Documents\test_l3.jpg")
width, height = 1500, 1300
pts1 = np.float32([[853, 158], [1892, 162], [581, 705], [1686, 734]])
#                   top left, top right, bottom left, bottom right
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("output image", imgOutput)
cv2.waitKey(0)
