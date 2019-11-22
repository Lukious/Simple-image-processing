import cv2

src = cv2.imread(".\\4x.png", cv2.IMREAD_COLOR)

dst = cv2.resize(src, dsize=(507, 334), interpolation=cv2.INTER_AREA)
#dst2 = cv2.resize(src, dsize=(0, 0), fx=0.5, fy=0.8, interpolation=cv2.INTER_LINEAR)

blur = cv2.GaussianBlur(dst,(5,5),0)

#cv2.imshow("src", src)
#cv2.imshow("dst", dst)
#cv2.imshow("dst2", dst2)
cv2.imwrite('rresized4.png', dst)
cv2.imwrite('blur_resice.png',blur)
#cv2.imshow("blured", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
