from matplotlib import pyplot
from bob.ip.flandmark import *
from bob.ip.draw import box, cross
from bob.ip.color import rgb_to_gray
import cv2
import numpy as np
	
lena = cv2.imread('Test3.jpg')
lena_gray = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)
faceCascade1 = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
localizer = Flandmark()
faces1 = faceCascade1.detectMultiScale(lena_gray, 1.1, 5)
for (x, y, w, h) in faces1:
    cv2.rectangle(lena, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_gray = lena_gray[y:y+h, x:x+w]
    roi_color = lena[y:y+h, x:x+w]
    keypoints = localizer.locate(lena_gray, x, y, w, h)

for k in keypoints:
	print(type((k[0],k[1])))
	cv2.circle(lena, (int(k[0]),int(k[1])), 1, (255, 255, 0), 2) # yellow key points
cv2.imwrite('Result6.jpg', lena);
#pyplot.imshow(lena.transpose(1, 2, 0))