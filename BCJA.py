#	[][][]	 [][][]  [][][]	  [][]
#	[]	[]	[]		   []	 []  []
#	[][][]	[]		   []   [][][][]
#	[]	 []	[]		[] []   []	  []
#	[][][]	 [][][]  [][]   []	  []
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

#Returns a 3 element array
def get_frontal_face_cascade():
	return getcascades.frontal_face()

def get_profile_face_cascade():
	return getcascades.profile_face()