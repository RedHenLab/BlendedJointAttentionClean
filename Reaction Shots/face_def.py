#!/bin/python

import numpy as np

class face(object):
	"""A Class to represent a face"""
	center = (0,0)
	width = 0
	height = 0
	vector = np.zeros((128,1))
	
	def __init__(self, center=(0,0), width=0, height=0, vector):
		""" Input params are (x,y) coords of center of face's bounding box, width
		    and height of box and the 128-dimensional vector representation of the face 
		""" 
		super(face, self).__init__()
		self.center = center
		self.width = width
		self.height = height
		self.vector = vector

	def compare(self, f2, dist=0):
		""" Compute similarity b/w two 128-D face vectors using any one of the following
			distance metric (can be chosen using value of 'dist':
			0 --> Euclidean distance
			1 --> Cosine distance
			// TODO: Check robustness of metrics. Waiting for data 
		"""
		
		v1 = self.vector
		v2 = f2.vector

		if dist == 1:  # Cosine distance
			return 1 - np.dot(v1,v2) / (np.linalg.norm(v1)*np.linalg.norm(v2))  # If the vectors are parallel, distance = 0		
		else:  # Euclidean distance (default)
			return np.linalg.norm(v1-v2)