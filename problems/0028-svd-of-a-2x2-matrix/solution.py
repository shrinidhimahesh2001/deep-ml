import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix.
    
    Args:
        A: 2x2 numpy array
    
    Returns:
        U: 2x2 orthogonal matrix (left singular vectors)
        s: 1D array of singular values
        V: 2x2 matrix (right singular vectors)
    """
    # Your code here
    At = np.transpose(A)
    AtA = At @ A
    eigenvalues , V = np.linalg.eig(AtA)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    V = V[:, idx]
    s = np.sqrt(np.maximum(eigenvalues, 0))
    U = A @ V
    for i in range(2):
        if s[i] > 1e-10:
            U[:, i] /= s[i]
    for i in range(2):
        if U[0, i] < 0:
            U[:, i] *= -1
            V[:, i] *= -1
    return U, s, np.transpose(V)
    pass