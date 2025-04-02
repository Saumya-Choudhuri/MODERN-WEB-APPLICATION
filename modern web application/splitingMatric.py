import numpy as np

def split_matrix(matrix):
    if matrix.shape[1] % 2 != 0:
        raise ValueError("Matrix must have an even number of columns to split equally.")
    
    mid = matrix.shape[1] // 2
    left_half = matrix[:, :mid] 
    right_half = matrix[:, mid:] 
    
    return left_half, right_half

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

left, right = split_matrix(matrix)

print("Left Half:\n", left)
print("Right Half:\n", right)
