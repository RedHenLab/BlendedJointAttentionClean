import cv2
import sys
import getcascades

def video_capture(height, width):
	cam = cv2.VideoCapture(-1)
	cam.set(3, width)
	cam.set(4, heigth)
	video_capture = cam
	return video_capture.read()

def face_detect_frontal(frame):

	faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
    faces2 = faceCascade2.detectMultiScale(gray, 1.1, 5)