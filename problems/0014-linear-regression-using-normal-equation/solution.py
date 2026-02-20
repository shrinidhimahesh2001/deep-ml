import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	#theta=[]
	X=np.array(X,dtype=float)
	y=np.array(y,dtype=float)
	X_transpose=np.transpose(X)
	X_invertible = np.linalg.inv(X_transpose @ X)
	theta = X_invertible@ X_transpose @ y

	theta[np.abs(theta) < 1e-10] = -0.0
	theta = np.round(theta,4)
	# Your code here, make sure to round
	return theta.tolist()