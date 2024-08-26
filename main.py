import cv2
import numpy as np


image = cv2.imread('file.webp')
image = cv2.resize(image, None, fx=0.55, fy=0.55)


def pencil_sketch_filter(img):
    gaussian_image = cv2.GaussianBlur(img, (3,3), 0)

    gray_image = cv2.cvtColor(gaussian_image, cv2.COLOR_BGR2GRAY)

    laplacian_image = cv2.Laplacian(gray_image, -1, ksize=3)

    ret, binary_inverse_image = cv2.threshold(laplacian_image, 13, 255, cv2.THRESH_BINARY_INV)

    return binary_inverse_image


def cartoon_filter(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    median_blur_image = cv2.medianBlur(gray_image, 1)

    get_edge_image = cv2.adaptiveThreshold(median_blur_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 4)

    bilateral_image = cv2.bilateralFilter(img, 9, 300, 300)

    final_image = cv2.bitwise_and(bilateral_image, bilateral_image, mask=get_edge_image)

    return final_image


pencil_sketch_image = pencil_sketch_filter(image)

cartoon_image = cartoon_filter(image)

cv2.imshow('Original', image)
cv2.imshow('Pencil Sketch Image', pencil_sketch_image)
cv2.imshow('Cartoonification Image', cartoon_image)

cv2.waitKey(0)

cv2.destroyAllWindows()