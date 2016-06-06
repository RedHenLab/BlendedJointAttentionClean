import cv2
import sys
import numpy as np

#import face cascades
faceCascade1 = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
faceCascade2 = cv2.CascadeClassifier('haarcascades/haarcascade_profileface.xml')
eyecascade1 = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
eyecascade2 = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')

frame = cv2.imread('Test_Images/Test2.jpg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
faces2 = faceCascade2.detectMultiScale(gray, 1.1, 5)

#Draw flag to check if a face is detected
flag = 0

# Draw a rectangle around the faces
for (x, y, w, h) in faces1:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    eyes1 = eyecascade1.detectMultiScale(gray, 1.5, 6)
    eyes2 = eyecascade2.detectMultiScale(gray, 1.5, 6)
    for (x1, y1, w1, h1 ) in eyes1:
		cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (128, 0, 127), 2)
		#extract eye (copy everywhere)
		split = frame[y1:y1+h1,x1:x1+w1]
		split = cv2.Canny(split,100,200)

		#detect circle (copy everywhere)
		circles = cv2.HoughCircles(split,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
		circles = np.uint16(np.around(circles))
		flag = 1
		for i in circles[0,:]:
			cv2.circle(split,(i[0],i[1]),i[2],(0,255,0),2)
			cv2.circle(split,(i[0],i[1]),2,(0,0,255),3)
			cv2.imwrite('Result_images/eye.jpg', split);
			print(1)
    if flag == 0:
        for (x2, y2, w2, h2 ) in eyes2:
			cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (0, 128, 127), 2)
			flag = 1
			split = frame[y2:y2+h2,x2:x2+w2]
			split = cv2.Canny(split,100,200)
			circles = cv2.HoughCircles(split,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
			circles = np.uint16(np.around(circles))
			for i in circles[0,:]:
				print(2)
				#draw the outer circle
				cv2.circle(split,(i[0],i[1]),i[2],(0,255,0),2)
				# draw the center of the circle
				cv2.circle(split,(i[0],i[1]),2,(0,0,255),3)
if flag == 0:
	for (x, y, w, h) in faces2:
		cv2.rectangle(frame, (x, y), (x+herew, y+h), (60, 60, 135), 2)
		eyes1 = eyecascade1.detectMultiScale(gray, 1.7, 6)
		eyes2 = eyecascade2.detectMultiScale(gray, 1.7, 6)
		for (x1, y1, w1, h1 ) in eyes1:
			cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (111, 111, 32), 2)
			flag = 1
			split = frame[y1:y1+h1, x1:x1+w1]
			if flag == 0 :
				for (x2, y2, w2, h2 ) in eyes2:
					cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (111, 32, 111), 2)
					split = frame[y2:y2+h2,x2:x2+w2]
# cv2.imwrite('Result_Images/Result2.jpg', frame);