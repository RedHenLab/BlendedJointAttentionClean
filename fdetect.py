import cv2
import sys
import getcascades

def video_capture(height, width):
	cam = cv2.VideoCapture(-1)
	cam.set(3, width)
	cam.set(4, heigth)
	video_capture = cam
	return video_capture.read()

def webcam_face_detect_frontal():
	facecascade = getcascades.frontal_face()
	while True:
		ret, frame = video_capture(480,640)
		if ret:
	        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	        for i in range(len(facecascade)):
	        	faces = facecascade[i].detectMultiScale(gray, 1.1, 5)
		        # Draw a rectangle around the faces
		        for (x, y, w, h) in faces:
		            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
	        # Display the resulting frame
	        cv2.imshow('Video', frame)
	        if cv2.waitKey(1) & 0xFF == ord('q'):
	            break
	# Release video capture
	video_capture.release()
	cv2.destroyAllWindows()
