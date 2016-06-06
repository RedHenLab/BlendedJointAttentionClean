import cv2
import sys
import getcascades

def video_read(height, width):
	cam = cv2.VideoCapture(-1)
	cam.set(3, width)
	cam.set(4, height)
	video_capture = cam
	return video_capture

def webcam_face_detect_frontal(facecascade):
	video = video_read(480,640)
	while True:
		ret, frame = video.read()
		if ret:
			for i in range(len(facecascade)):
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				faces = facecascade[i].detectMultiScale(gray, 1.1, 5)
		        # Draw a rectangle around the faces
		        for (x, y, w, h) in faces:
		            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
		            print("true")
	        # Display the resulting frame
	        # print(type(frame))
	        if frame.any()>0:
	        	cv2.imshow('Video', frame)
	        if cv2.waitKey(1) & 0xFF == ord('q'):
	            break
	# Release video capture
	video.release()
	cv2.destroyAllWindows()
