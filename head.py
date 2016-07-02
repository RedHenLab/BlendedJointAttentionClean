import cv2
import dlib 
import fdetect

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlibcascades/shape_predictor_68_face_landmarks.dat')

def face_pose(video_capture,facecascade):
	video = fdetect.video_read(480,640)
	while True:
	    # Capture frame-by-frame
		ret, frame = video_capture.read()
		if ret:
			dets = detector(frame, 1)
			for k, d in enumerate(dets):
			    # Get the landmarks/parts for the face in box d.
				shape = predictor(frame, d)
				mid_x = [(shape.part(1).x+shape.part(15).x)/2, (shape.part(1).y+shape.part(15).y)/2]
				mid_y = [(shape.part(27).x+shape.part(66).x)/2, (shape.part(27).y+shape.part(66).y)/2]
				nose = [shape.part(30).x,shape.part(30).y]
				final_x = 3*nose[0]-2*mid_x[0]
				final_y = 3*nose[1]-2*mid_y[1]
				# print nose,final_x
				cv2.circle(frame,(final_x,final_y),2,(0,0,255))
				cv2.circle(frame,(nose[0],nose[1]),2,(0,0,255))
				cv2.line(frame,(nose[0],nose[1]), (final_x,final_y),(255,0,0),3)
		# Display the resulting frame
		cv2.imshow('Video', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
		    break
	# Release video capture
	video.release()
	cv2.destroyAllWindows()