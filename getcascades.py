import cv2
import dlib

def frontal_face():
	faceCascade1 = cv2.CascadeClassifier('Cascades/haarcascades/haarcascade_frontalface_alt2.xml')
	faceCascade2 = cv2.CascadeClassifier('Cascades/haarcascades/haarcascade_frontalface_default.xml')
	faceCascade3 = cv2.CascadeClassifier('Cascades/haarcascades/haarcascade_frontalface_alt.xml')
	return [faceCascade1,faceCascade2,faceCascade3]

def profile_face():
	faceCascade1 = cv2.CascadeClassifier('Cascades/haarcascades/haarcascade_profileface.xml')
	faceCascade2 = cv2.CascadeClassifier('Cascades/lbp_cascades/lbpcascade_profileface.xml')
	return [faceCascade1,faceCascade2]

def facial_landmarks():
	predictor = dlib.shape_predictor('Cascades/dlibcascades/shape_predictor_68_face_landmarks.dat')
	return predictor