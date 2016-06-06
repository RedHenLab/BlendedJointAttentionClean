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
    		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    		eyes1 = eyecascade1.detectMultiScale(gray, 1.5, 6)
    		for (x1, y1, w1, h1 ) in eyes1:
				split = frame[y1:y1+h1,x1:x1+w1]
				detector = cv2.SimpleBlobDetector_create()
				cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (122, 123, 0), 2)
				# Detect blobs.
				keypoints = detector.detect(split)
				# Draw detected blobs as red circles.
				# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
				if(len(keypoints)!=0):
					print(keypoints)
					split = cv2.drawKeypoints(split , keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
		# Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
