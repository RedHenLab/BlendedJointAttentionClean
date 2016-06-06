import sys
import os
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlibcascades/shape_predictor_68_face_landmarks.dat')

cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

while True:
    ret, frame = video_capture.read()
    if ret:
	    # win.clear_overlay()
	    # win.set_image(frame)

	    dets = detector(frame, 1)
	    for k, d in enumerate(dets):
	        # Get the landmarks/parts for the face in box d.
	        shape = predictor(frame, d)
	        # print(type(shape.part(1).x))
	        cv2.circle(frame,(shape.part(36).x,shape.part(36).y),2,(0,0,255))
	        cv2.circle(frame,(shape.part(39).x,shape.part(39).y),2,(0,0,255))
	        cv2.circle(frame,(shape.part(42).x,shape.part(42).y),2,(0,0,255))
	        cv2.circle(frame,(shape.part(45).x,shape.part(45).y),2,(0,0,255))
	        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
        	break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()

	        