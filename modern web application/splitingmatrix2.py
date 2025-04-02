import numpy as np

# Define a 4x4 matrix
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

mid = matrix.shape[1] // 2

left_half = matrix[:, :mid]
right_half = matrix[:, mid:]

# Print the results
print("Original 4x4 Matrix:")
print(matrix)

print("\nLeft Half (First 2 Columns):")
print(left_half)

print("\nRight Half (Last 2 Columns):")
print(right_half)
