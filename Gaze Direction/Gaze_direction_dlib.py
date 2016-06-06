#Fabian implementation

import cv2
import numpy as np
from matplotlib import pyplot as plt
import dlib 

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlibcascades/shape_predictor_68_face_landmarks.dat')


while True:
    # Capture frame-by-frame
	ret, frame = video_capture.read()
	if ret:
		dets = detector(frame, 1)
		for k, d in enumerate(dets):
	        # Get the landmarks/parts for the face in box d.
			shape = predictor(frame, d)
	        # print(type(shape.part(1).x))
			cv2.circle(frame,(shape.part(36).x,shape.part(36).y),2,(0,0,255))
			cv2.circle(frame,(shape.part(39).x,shape.part(39).y),2,(0,0,255))
			cv2.circle(frame,(shape.part(42).x,shape.part(42).y),2,(0,0,255))
			cv2.circle(frame,(shape.part(45).x,shape.part(45).y),2,(0,0,255))
			x1 = shape.part(36).x
			y1 = shape.part(37).y
			x2 = shape.part(39).x
			y2 = shape.part(40).y
			split = frame[y1:y2,x1:x2]
			split1=cv2.cvtColor(split, cv2.COLOR_BGR2GRAY)
			sobelx = cv2.Sobel(split1,cv2.CV_64F,1,0,ksize=5)
			sobely = cv2.Sobel(split1,cv2.CV_64F,0,1,ksize=5)
			sob = np.multiply(sobelx,sobely)
			minin = 10000
			minj=0
			mini=0
			print(sob.shape)
			for i in range(len(sob)):
				for j in range(len(sob)):
					if(sob[int(i)][int(j)]<minin):
						minin=split1[i][j]
						mini=i
						minj=j
						print(mini,minj)
			
			cv2.circle(frame,(x1+mini,y1+minj),1,(0,0,255))						
			cv2.line(frame,(x1+mini,y1+minj), (int((3*x1+4*mini-x2)/2),int((3*y1+4*minj-y2)/2)),(255,0,0))
			x1 = shape.part(42).x
			y1 = shape.part(43).y
			x2 = shape.part(45).x
			y2 = shape.part(46).y
			split = frame[y1:y2,x1:x2]
			split1=cv2.cvtColor(split, cv2.COLOR_BGR2GRAY)
			sobelx = cv2.Sobel(split1,cv2.CV_64F,1,0,ksize=5)
			sobely = cv2.Sobel(split1,cv2.CV_64F,0,1,ksize=5)
			sob = np.multiply(sobelx,sobely)
			minin = 10000
			minj=0
			mini=0
			print(sob.shape)
			for i in range(len(sob)):
				for j in range(len(sob)):
					if(sob[int(i)][int(j)]<minin):
						minin=split1[i][j]
						mini=i
						minj=j
						print(mini,minj)
			
			cv2.circle(frame,(x1+mini,y1+minj),1,(0,0,255))						
			cv2.line(frame,(x1+mini,y1+minj), (int((3*x1+4*mini-x2)/2),int((3*y1+4*minj-y2)/2)),(255,0,0))
		# Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
