import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a=np.array(a)
	if a.size ==np.prod(new_shape):
		reshaped_matrix=np.reshape(a,new_shape)
	else:
		reshaped_matrix = []
	return reshaped_matrix