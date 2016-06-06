import cv2
import sys

# Defining cascade variables
faceCascade1 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

frame_number = 0
flag = 0
last_x = 0
last_y = 0
last_w = 0
last_h = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:
        if flag == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces1:
                template = gray[y:y+h, x:x+w]
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                roi_gray = gray[(y-10):(y+h+10), (x-10):(x+w+10)]
                roi_gray2 = gray[(y-20):(y+h+20), (x-20):(x+w+20)]
                last_x = x
                last_y = y
                last_h = h
                last_w = w
                flag = 1
                frame_number=frame_number+1

        else :
            flag = 0
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces1 = faceCascade1.detectMultiScale(roi_gray, 1.1, 5)
            
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces1:
                x = last_x+x-10
                y = last_y+y-10
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[(y-10):(y+h+10), (x-10):(x+w+10)]
                roi_gray2 = gray[(y-20):(y+h+20), (x-20):(x+w+20)]
                template = gray[y:y+h, x:x+w]
                last_x = x
                last_y = y
                last_h = h
                last_w = w
                flag = 1
                frame_number=frame_number+1

        if flag == 0 and frame_number != 0:
            # Apply template Matching
            res = cv2.matchTemplate(roi_gray2,template,cv2.TM_CCOEFF)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            top_left = (top_left[0]+last_x-10, top_left[1]+last_y-10)
            bottom_right = (top_left[0] + last_w, top_left[1] + last_h)
            cv2.rectangle(frame,top_left, bottom_right, (0,255,0), 2)
            roi_gray = gray[top_left[1]-10:top_left[1]+last_h+10, top_left[0]-10:(top_left[0]+last_w+10)]
            frame_number = frame_number + 1
        # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        print(frame_number)
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
