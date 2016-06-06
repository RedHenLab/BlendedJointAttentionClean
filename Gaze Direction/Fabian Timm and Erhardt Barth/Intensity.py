import cv2
import numpy as np

img = cv2.imread('../Result_Images/eye1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
minin = 1000000
minj=0
mini=0
for i in range(gray.shape[0]):
	for j in range(gray.shape[1]):
		if (gray[i][j]<minin):
			minin=gray[i][j]
			mini=i
			minj=j
			print(mini,minj)

cv2.circle(img,(mini,minj),4,(0,0,255))
cv2.imwrite('../Result_Images/eye2.jpg', img);
