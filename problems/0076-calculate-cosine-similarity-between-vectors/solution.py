import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	normv1 = np.linalg.norm(v1)
	normv2 = np.linalg.norm(v2)
	dotprod = v1 @ v2
	costheta = dotprod / (normv1 * normv2)
	return costheta
	pass