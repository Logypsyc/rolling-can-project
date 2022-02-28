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


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, str(x) + ',' + str(y), (x, y), font, 1, (0, 0, 255), 2)
        cv2.imshow('image', image)


# driver function
if __name__ == "__main__":
    # reading the image
    image = cv2.imread("/Users/local/PycharmProjects/findcircles_kennethlin/test_l3.jpg")

    # displaying the image
    cv2.imshow('image', image)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
