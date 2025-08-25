import numpy

A = numpy.array([[8, 9], [5, 3]])
B = numpy.array([[1, 5], [6, 27]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix addition
D = A + B
print("\nA + B:\n", D)  

# Matrix multiplication
C = numpy.dot(A, B)  
print("\nA x B:\n", C)

# Transpose
print("\nTranspose of A:\n", A.T)

# Determinant
det_A = numpy.linalg.det(A)
print("\nDeterminant of A:", det_A)


if det_A != 0:
    inv_A = numpy.linalg.inv(A)
    print("\nInverse of A:\n", inv_A)
else:
    print("\nMatrix A is singular, no inverse exists.")