import cv2
import numpy as np

img = cv2.imread('Test_Images/News.jpg')
img1 = img

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.Canny(img,100,200)
cv2.imwrite('Result_Images/Temp.jpg', thresh)
# ret,thresh = cv2.threshold(img,127,255,0)
_, contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

rect = 0
for i in range(len(contours)):
	cnt = contours[i]
	M = cv2.moments(cnt)
	# print M
	
	if(M['m00']!=0):
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])


		epsilon = 0.1*cv2.arcLength(cnt,True)
		approx = cv2.approxPolyDP(cnt,epsilon,True)
		if(len(approx)==4 and epsilon>7):
			rect = rect + 1
			cv2.drawContours(img1, contours[i], -1, (0,0,255), 2)

print(rect)
cv2.imwrite('Result_Images/News.jpg', img1)