# -*- coding: utf-8 -*-

import sys
import cv2
import os
from os import listdir
from os.path import isfile, join



files = [f for f in listdir('.\\layerstructure') if isfile(join('.\\layerstructure', f))]


#w_path = os.listdir('C:\\Users\\lukious\\Desktop\\PythonOCR\\layerstructure')
#print(w_path)



print("Python version: \n" + sys.version)
print("cv2 version: " + cv2.__version__)
print(files)


for i in files:
	front = '.\\'
	end = i
	result_in = front + end
	result_out = '.\\converted\\'+ 'converted_'+ end
	print(result_in)
	img1 = cv2.imread(result_in, 1)
	hsv1 = cv2.cvtColor(img1, cv2.COLOR_RGB2HSV)
	h,s,v = cv2.split(hsv1)
	#hsv2 = cv2.merge((h,s,v))
	#img2 = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)
	#cv2.imshow('img1',img1)
	#cv2.imshow('hsv1',hsv1)
	#cv2.imshow('h', h)
	#cv2.imshow('s', s)
	cv2.imshow('v', v)
	#cv2.imshow('hsv2',hsv2)
	#cv2.imshow('img2',img2)
	cv2.imwrite(result_out, v)

#cv2.waitKey(0)

