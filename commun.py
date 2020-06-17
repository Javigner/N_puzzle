import numpy as np

def spiral_traversal(matrix):
    res = []
    while matrix.size:
        res.append(matrix[0])  # take first row
        matrix = matrix[1:].T[::-1]  # cut off first row and rotate counterclockwise
    return np.concatenate(res)