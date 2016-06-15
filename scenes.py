import cv2

def scene_change(input_file):
	cap = cv2.VideoCapture(input_file)
	video_capture = cap
	cv2.ocl.setUseOpenCL(False)
	fgbg = cv2.createBackgroundSubtractorMOG2()
	frame_num = 0
	last_detected = -20
	scene_num = 0
	while(1):
		frame_num = frame_num + 1
		ret, frame = video_capture.read()
		fgmask = fgbg.apply(frame)
		num_white = 0
		flag = 0
		if(frame_num-last_detected>40):
			last_detected = frame_num
			for i in range(fgmask.shape[0]):
				for j in range(fgmask.shape[1]):
					if fgmask[i][j] == 255:
						num_white = num_white+1
						if(num_white>0.8*fgmask.shape[0]*fgmask.shape[0]):
							scene_num = scene_num + 1
							print("Scene changed : ", scene_num)
							flag = 1
							break
				if flag == 1:
					break
		cv2.imshow('Video',fgmask)
		cv2.imshow('Video',frame)
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			break
	cap.release()
	cv2.destroyAllWindows()