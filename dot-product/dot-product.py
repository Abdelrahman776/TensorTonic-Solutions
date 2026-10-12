import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write fcode here
    # x= np.ndarray(x, dtype=float)
    # y= np.ndarray(y, dtype=float)
    sum=0.0
    # sum=np.dot(x,y)
    for i in range(len(x)):
        sum+= (x[i]*y[i])
    return float(sum)