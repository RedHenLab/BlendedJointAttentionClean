# 
#    _ _ _     _ _ _ _   _ _ _ _   _ _ _ _ 
#   /\  _ `\  /\  _ _ _\/\_ _ _  \/\  _ _ `\
#   \ \ \_\ \_\ \ \_ _ /\/_ _ _/\ \ \ \   \ \
#    \ \  _ _ `\ \ \        _  \ \ \ \ \_ _\ \
#     \ \ \_ _\ \ \ \_ _ _ /\`\_\/  \ \  _ _  \
#      \ \_ _ _ _\ \_ _ _ _\ \_ _ _ _\ \_\_ /\_\
#       \/_ _ _ _/\/_ _ _ _/\/_ _ _ _/\/_/  \/_/ 
#
#	================================================
# 	Library used to detect facial features, gestures
#	and other thigs, finally used to detect and cla-
#	-ssify different instances of blended classical
#	joint attention. For further information and us-
#	-age see ReadMe.md. 
#	================================================
#
#	Liscence is hereby provided to everyone abiding
#	by the liscecnces of the dependencies to use this
#	library when and where needed without a need to 
# 	state. 
#	================================================

import fdetect
import getcascades

# Returns a 3 element array (used for internal functions only)
def get_frontal_face_cascade():
	return getcascades.frontal_face()

# Returns a 2 element array (used for internal functions only)
def get_profile_face_cascade():
	return getcascades.profile_face()

# Returns a 2 element array (used for internal functions only)
def get_facial_landmarks():
	return getcascades.facial_landmarks()

# Takes input from webcam and detects a single frontal face out of many
def get_webcam_frontal_face_single():
	facecascade = get_frontal_face_cascade()
	fdetect.webcam_face_detect_single(facecascade)

# Takes input from webcam and detects all frontal faces
def get_webcam_frontal_face():
	facecascade = get_frontal_face_cascade()
	fdetect.webcam_face_detect(facecascade)

# Takes input from webcam and detects a single profile face out of many
def get_webcam_profile_face_single():
	facecascade = get_profile_face_cascade()
	fdetect.webcam_face_detect_single(facecascade)

# Takes input from webcam and detects all profile faces
def get_webcam_profile_face():
	facecascade = get_profile_face_cascade()
	fdetect.webcam_face_detect(facecascade)

# Takes input from webcam and detects single face of all kinds
def get_webcam__face():
	acecascade = [get_profile_face_cascade().get_frontal_face_cascade()]
	fdetect.webcam_face_detect_single(facecascade)

# Takes input from webcam and detects all face of all kinds
def get_webcam__face():
	acecascade = [get_profile_face_cascade().get_frontal_face_cascade()]
	fdetect.webcam_face_detect_single(facecascade)

# Takes input from webcam and detects a single face of any kind with template matching boost
def get_webcam_face_template():
	facecascade = [get_profile_face_cascade().get_frontal_face_cascade()]
	fdetect.webcam_face_detect_template_matching(facecascade)

