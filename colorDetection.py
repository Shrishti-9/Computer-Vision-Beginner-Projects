import cv2
import numpy as np

img = cv2.imread('colorful.jfif')
img = cv2.resize(img, None, fx=1.5, fy=1.5)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def empty(s):
    pass


cv2.namedWindow('HSV')
cv2.resizeWindow('HSV', 640, 240)
cv2.createTrackbar('Hue Min', 'HSV', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'HSV', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'HSV', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'HSV', 255, 255, empty)
cv2.createTrackbar('Value Min', 'HSV', 0, 255, empty)
cv2.createTrackbar('Value Max', 'HSV', 255, 255, empty)


while True:
    hue_min = cv2.getTrackbarPos('Hue Min', 'HSV')
    hue_max = cv2.getTrackbarPos('Hue Max', 'HSV')
    sat_min = cv2.getTrackbarPos('Sat Min', 'HSV')
    sat_max = cv2.getTrackbarPos('Sat Max', 'HSV')
    value_min = cv2.getTrackbarPos('Value Min', 'HSV')
    value_max = cv2.getTrackbarPos('Value Max', 'HSV')

    lower = np.array([hue_min, sat_min, value_min])
    upper = np.array([hue_max, sat_max, value_max])

    mask = cv2.inRange(img_hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    hstack = np.hstack([img, result])

    cv2.imshow('Final Result', hstack)
    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()