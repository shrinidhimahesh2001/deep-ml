import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	covariance=[]
	covariance=np.cov(vectors)
	return covariance.tolist()