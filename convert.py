"""importing the dependencies"""
import cv2

"""reading the image and saving it to image variable"""
image = cv2.imread("5.jpg")

"""applying the grey filter on the image inputed"""
grey_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

"""inverting the grey image"""
invert = cv2.bitwise_not(grey_filter)

"""Applying the blur to the inverted image"""
blur = cv2.GaussianBlur(invert, (29,29), 500)

"""inverting the blurred image"""
invertedBlur = cv2.bitwise_not(blur)

"""merging all the filtred image"""
sketch_filter = cv2.divide(grey_filter, invertedBlur, scale=250.0)

"""saving the result as output"""
cv2.imwrite("output9.png", sketch_filter)
