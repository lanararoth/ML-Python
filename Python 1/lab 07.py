import numpy as np

# dimensions of the matrix A
rowsa = int(input("Enter number of rows A: "))
colsa = int(input("Enter number of columns A: "))

# dimensions of the matrix A
rowsb = int(input("Enter number of rows B: "))
colsb = int(input("Enter number of columns B: "))

# matrix A
print(f"Enter elements of Matrix A ({rowsa}x{colsa}):")
A = []
for i in range(rowsa):
    row = list(map(int, input().split()))
    A.append(row)
A = np.array(A)

# matrix B 
print(f"Enter elements of Matrix B ({rowsb}x{colsb}):")
B = []
for i in range(rowsb):
    row = list(map(int, input().split()))
    B.append(row)
B = np.array(B)

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

# Matrix Addition (only possible if same dimensions)
if A.shape == B.shape:
    D = A + B
    print("\nA + B:\n", D)
else:
    print("\nMatrix addition not possible (different dimensions)")

# Matrix Multiplication (possible if cols of A = rows of B)
if A.shape[1] == B.shape[0]:
    C = np.dot(A, B)
    print("\nA x B:\n", C)
else:
    print("\nMatrix multiplication not possible (columns of A != rows of B)")

# Transpose
print("\nTranspose of A:\n", A.T)

# Determinant & Inverse (only for square matrices)
if A.shape[0] == A.shape[1]:
    detA = np.linalg.det(A)

    print("\nDeterminant of A:", detA)

    if detA != 0:
        invA = np.linalg.inv(A)
        print("\nInverse of A:\n", invA)
    else:
        print("\nMatrix A is singular, no inverse exists")
else:
    print("\nDeterminant and Inverse are not defined for non-square matrices")
