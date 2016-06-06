import cv2
import sys

# Defining cascade variables
faceCascade1 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')
nosecascade = cv2.CascadeClassifier('../haarcascades/haarcascade_mcs_nose.xml')

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam
a = list()
b = list()
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces1:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            nose = nosecascade.detectMultiScale(roi_gray,1.3,5)
            for (ex,ey,ew,eh) in nose:
               cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,0),2)
               a.append(ex+ew/2)
               b.append(ey+eh/2)
        # Display the resulting frame
        for i in range(len(a)):
            cv2.circle(frame, (x+a[i],y+b[i]),1,(128,0,127),2)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
