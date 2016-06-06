#Done by intensity.py

#Poor accuracy

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
				minin = 1000000
				minj=0
				mini=0
				for i in range(split1.shape[0]):
					for j in range(split1.shape[1]):
						if (split1[i][j]<minin):
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
