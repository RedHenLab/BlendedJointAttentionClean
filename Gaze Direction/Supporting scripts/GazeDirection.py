import cv2
import sys
import numpy as np

#import face cascades
faceCascade1 = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
faceCascade2 = cv2.CascadeClassifier('haarcascades/haarcascade_profileface.xml')
eyecascade1 = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
eyecascade2 = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')

frame = cv2.imread('Test_Images/Test3.jpg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
detector = cv2.SimpleBlobDetector_create()
faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
faces2 = faceCascade2.detectMultiScale(gray, 1.1, 5)
# Draw a rectangle around the faces
flag = 0
for (x, y, w, h) in faces1:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    eyes1 = eyecascade1.detectMultiScale(gray, 1.5, 6)
    eyes2 = eyecascade2.detectMultiScale(gray, 1.5, 6)
    for (x1, y1, w1, h1 ) in eyes1:
		cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (128, 0, 127), 2)
		split = frame[y1:y1+h1,x1:x1+w1]
		keypoints = detector.detect(split)
		cv2.circle(split, [int(x1),int(y1+h1/2)],[int(x1+w1), int(y1+h1/2)], 1)
		for kp in keypoints :
   			cv2.circle(split, [int(kp.pt[0]),int(kp.pt[1])], 1)
		flag = 1

    if flag == 0:
        for (x2, y2, w2, h2 ) in eyes2:
			cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (0, 128, 127), 2)
			split = frame[y2:y2+h2,x2:x2+w2]
			keypoints = detector.detect(split)
			cv2.circle(split, [int(x1),int(y1+h1/2)],[int(x1+w1), int(y1+h1/2)], 1)
			for kp in keypoints :
	   			cv2.circle(split, [int(kp.pt[0]),int(kp.pt[1])], 1)
			flag = 1

if flag == 0:
	for (x, y, w, h) in faces2:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (60, 60, 135), 2)
		eyes1 = eyecascade1.detectMultiScale(gray, 1.7, 6)
		eyes2 = eyecascade2.detectMultiScale(gray, 1.7, 6)
		for (x1, y1, w1, h1 ) in eyes1:
			cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (111, 111, 32), 2)
			split = frame[y1:y1+h1, x1:x1+w1]
			keypoints = detector.detect(split)
			cv2.circle(split, [int(x1),int(y1+h1/2)],[int(x1+w1), int(y1+h1/2)], 1)
			for kp in keypoints :
	   			cv2.circle(split, [int(kp.pt[0]),int(kp.pt[1])], 1)
			flag = 1

			if flag == 0 :
				for (x2, y2, w2, h2 ) in eyes2:
					cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (111, 32, 111), 2)
					split = frame[y2:y2+h2,x2:x2+w2]
					keypoints = detector.detect(split)
					cv2.circle(split, [int(x1),int(y1+h1/2)],[int(x1+w1), int(y1+h1/2)], 1)
					for kp in keypoints :
			   			cv2.circle(split, [int(kp.pt[0]),int(kp.pt[1])], 1)
					flag = 1
cv2.imwrite("Result_Images/Result_Gaze_1.jpg", split)