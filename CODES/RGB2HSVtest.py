# -*- coding: utf-8 -*-

import sys
import cv2

print("Python version: \n" + sys.version)
print("cv2 version: " + cv2.__version__)


img1 = cv2.imread('C:\\Users\\lukious\\Desktop\\PythonOCR\\layer1.png', 1)
hsv1 = cv2.cvtColor(img1, cv2.COLOR_RGB2HSV)
h,s,v = cv2.split(hsv1)
hsv2 = cv2.merge((h,s,v))
img2 = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)

cv2.imshow('img1',img1)
cv2.imshow('hsv1',hsv1)
cv2.imshow('h', h)
cv2.imshow('s', s)
cv2.imshow('v', v)
cv2.imshow('hsv2',hsv2)
cv2.imshow('img2',img2)

cv2.imwrite('layer1hsv.jpg', v)


cv2.waitKey(0)


