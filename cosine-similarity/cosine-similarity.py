import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a=np.asarray(a, dtype=float)
    b=np.asarray(b, dtype=float)
    norm_a=np.linalg.norm(a)
    norm_b=np.linalg.norm(b)

    norm_2 =float(norm_a*norm_b)
    if norm_2==0:
        return 0.0
    return float(np.dot(a,b))/norm_2
    