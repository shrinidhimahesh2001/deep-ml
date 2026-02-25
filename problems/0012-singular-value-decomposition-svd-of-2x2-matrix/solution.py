import numpy as np
def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    # Your code here
    A = np.array(A, dtype=float)
    At = np.transpose(A)
    B = At @ A
    a=B[0,0]
    b=B[0,1]
    d=B[1,1]
    two_theta = np.arctan2(2*b,a - d)
    theta = two_theta * 0.5
    c = np.cos(theta)
    s = np.sin(theta)
    R = np.array([[c, -s],[s,  c]])
    D = R.T @ B @ R
    S= np.sqrt(np.maximum(D.diagonal(), 0))
    V = R
    #Vt = R.T
    if S[0] < S[1]:
        S = S[::-1]
        V = V[:, ::-1]
    Vt = V.T
    U = np.zeros((2, 2))
    for i in range(2):
        if S[i] > 1e-10:
            U[:, i] = A @ V[:, i] / S[i]
        else:
            # Handle zero singula