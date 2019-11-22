import cv2

# Load an color image in grayscale
img = cv2.imread('.\\layer1.png',0)
ret, thresh_img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY_INV)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
cv2.THRESH_BINARY,15,2)
cv2.imshow('grey image',thresh_img)
cv2.imshow('gaussian image', th3)
cv2.imwrite("result11.jpg", thresh_img)
cv2.imwrite("result12.png",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()