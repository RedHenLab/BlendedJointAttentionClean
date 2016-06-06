#Done by Laplacian.py

#Average accuracy

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

#extract eye image

faceCascade1 = cv2.CascadeClassifier('../../haarcascades/haarcascade_frontalface_alt2.xml')
eyecascade1 = cv2.CascadeClassifier('../../haarcascades/haarcascade_eye.xml')

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:

    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
    	for (x, y, w, h) in faces1:
		    eyes1 = eyecascade1.detectMultiScale(gray, 1.5, 6)
		    for (x1, y1, w1, h1 ) in eyes1:
				split = frame[y1:y1+h1,x1:x1+w1]
				split1=cv2.cvtColor(split, cv2.COLOR_BGR2GRAY)
				laplacian = cv2.Laplacian(split1,cv2.CV_64F)
				minin = 100000
				minj=0
				mini=0
				print(laplacian.shape)
				for i in range(len(laplacian)/2):
					for j in range(len(laplacian)/2):
						if(laplacian[int(i+len(laplacian)/4)][int(j+len(laplacian)/4)]<minin):
							minin=gray[i][j]
							mini=i
							minj=j
							print(mini,minj)
				cv2.circle(frame,(x1+mini,y1+minj),4,(0,0,255))						

		# Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
