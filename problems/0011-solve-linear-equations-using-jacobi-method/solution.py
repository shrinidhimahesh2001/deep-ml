import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:

	size = len(b)
	A = np.array(A, dtype=float)
	b = np.array(b, dtype=float)
	x = np.zeros(size)
	#x = b.astype(float)

	for _ in range (n):
		x_new = np.zeros(size)
		for i in range (size):
			s=0
			for j in range(size):
				if j != i:
					s += A[i][j] * x[j]
			x_new[i] = (b[i] - s) / A[i][i]
			#x[i]=(1/A[i][i])*(b[i]-sum(a[i][j]*x[j]))
		#x = x_new.copy()
		x = np.round(x_new, 4)
	return x.tolist()