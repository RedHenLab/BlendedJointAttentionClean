import cv2


def frontal_face():
	faceCascade1 = cv2.CascadeClassifier('cascades/haarcascades/haarcascade_frontalface_alt2.xml')
	faceCascade2 = cv2.CascadeClassifier('cascades/haarcascades/haarcascade_frontalface_default.xml')
	faceCascade3 = cv2.CascadeClassifier('cascades/haarcascades/haarcascade_frontalface_alt.xml')
	return [faceCascade1,faceCascade2,faceCascade3]

def profile_face():
	faceCascade1 = cv2.CascadeClassifier('cascades/haarcascades/haarcascade_profileface.xml')
	faceCascade2 = cv2.CascadeClassifier('cascades/lbp_cascades/lbpcascade_profileface.xml')
