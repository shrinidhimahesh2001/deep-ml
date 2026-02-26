import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	B=np.array(B)
	C=np.array(C)
	C_inv = np.linalg.inv(C)
	P= C_inv @ B
	P=np.round(P,4)
	return P.tolist()