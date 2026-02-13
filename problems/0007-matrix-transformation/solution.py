import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A=np.array(A)
	T=np.array(T)
	S=np.array(S)
	detT = np.linalg.det(T)
	detS = np.linalg.det(S)
	if detT!=0 and detS!=0:
		T_inv=np.linalg.inv(T)
		transformed_matrix = T_inv@A@S
	else:
		transformed_matrix = -1
	return transformed_matrix