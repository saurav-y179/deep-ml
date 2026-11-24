import numpy as np

def calculate_dot_product(vec1, vec2):
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The dot product of the two vectors.
    """
    # Your code here
    v1 =  np.array(vec1)
    v2 = np.array(vec2)
    return v1@v2
    pass