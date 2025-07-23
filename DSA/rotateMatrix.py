# Function to rotate the matrix 90 degrees clockwise
def rotate(mat):
    n = len(mat)

    # Step 1: Transpose the matrix
    for i in range(n - 1):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        mat[i].reverse()


# Sample input matrix
matrix = [
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# Rotate the matrix
rotate(matrix)

print("\nRotated Matrix by 90 degrees:")
for row in matrix:
    print(row)
