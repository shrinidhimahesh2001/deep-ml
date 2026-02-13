import numpy as np
def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    a=np.array(a)
    b=np.array(b)
    if a.shape[1] == b.shape[0]:
        c=np.matmul(a,b)
    else:
        c = -1
    return c