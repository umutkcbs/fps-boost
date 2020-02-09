import cv2
import os

x = str(0)

while True:
	isim1 = 'frame' + x + '.jpg'
	x = str(int(x) + 2)
	isim2 = 'frame' + x + '.jpg'
	img1 = cv2.imread(isim1)
	img2 = cv2.imread(isim2)
	add = cv2.addWeighted(img1,0.5,img2,0.5,0)
	s = str(int(x) - 1)
	cv2.imwrite('frame' + s + '.jpg', add)

#cv2.imshow('Addition', add)

#cv2.waitKey(0)
#cv2.destroyAllWindows()