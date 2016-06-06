import cv2
import sys

#import face cascades
faceCascade1 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')
faceCascade2 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
faceCascade3 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt.xml')
faceCascade5 = cv2.CascadeClassifier('../haarcascades/haarcascade_profileface.xml')
faceCascade6 = cv2.CascadeClassifier('../lbp_cascades/lbpcascade_profileface.xml')

frame = cv2.imread('Test_Images/Test8.jpg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
faces2 = faceCascade2.detectMultiScale(gray, 1.1, 5)
faces3 = faceCascade3.detectMultiScale(gray, 1.1, 5)
faces5 = faceCascade5.detectMultiScale(gray, 1.1, 5)
faces6 = faceCascade6.detectMultiScale(gray, 1.1, 5)

# Draw a rectangle around the faces
for (x, y, w, h) in faces1:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
for (x, y, w, h) in faces2:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
for (x, y, w, h) in faces3:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (127, 128, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
for (x, y, w, h) in faces5:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (127, 128, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
for (x, y, w, h) in faces6:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (127, 128, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
cv2.imwrite('Result_Images/Result8.jpg', frame);