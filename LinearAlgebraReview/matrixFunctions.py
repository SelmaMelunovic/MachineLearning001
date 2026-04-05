#Matrix Size function
from pandas.core.dtypes.common import is_datetime64_ns_dtype


def size(x):
    rows = len(x)

    if rows > 0:
        if type(x[0]) != list:
            raise RuntimeError('matrix should be list of lists')

        cols = len(x[0])
        return rows,cols
    else:
        return 0,0


# Generate Function -> creates a matrix filled with default value

def generate(rows, columns, default_value=0):
    return [[default_value for _ in range(columns)] for _ in range(rows)]

# Scalar Multiplication function -> multiplies every element by a number

def scalar_mul(num, A):
    return [[num * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Scalar Addition function -> Adds a number to every element

def scalar_add(num, A):
    return [[num + A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# Matrix Multiplication function -> Multiplies matrices, columns of A must be equal to rows of B

def mul(A,B):
    rows_A, cols_A = size(A)
    rows_B, cols_B = size(B)

    if cols_A != rows_B:
        raise RuntimeError('Cannot multiply: columns of A must be equal to rows of B')

    result = generate(rows_A, cols_B)
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Concat Function -> Joins two matrices side by side, rows must match

def concat(A,B):
    rows_A, _ = size(A)
    rows_B, _ = size(B)

    if rows_A != rows_B:
        raise RuntimeError('Cannot concatenate: number of rows must match')

    return [A[i] + B[i] for i in range(rows_A)]

#Addition and Subtraction function -> Element-wise addition and subtraction, matrices must be same size

def add(A, B):
    rows, cols = size(A)
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

def sub(A, B):
    rows, cols = size(A)
    return [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]

# Sum and Product function

def sum_el(A):
    total = 0
    for row in A:
        for val in row:
            total += val
    return total

def prod_el(A):
    total = 1
    for row in A:
        for val in row:
            total *= val
    return total

#Transpose function -> rows become columns

def trans(A):
    rows, cols = size(A)
    return [[A[i][j] for i in range(rows)] for j in range(cols)]

#Identity Matrix -> 1s on diagonal, 0s everywhere else

def identity(mtx):
    rows, _ = size(mtx)
    return [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]

#Minor Function -> remove a row and column

def minor(mtx, row, column):
    return [
        [mtx[i][j] for j in range(len(mtx[0])) if j != column]
        for i in range(len(mtx)) if i != row
    ]

#Determinant function

def determinant(mtx):
    rows, cols = size(mtx)

    if rows != cols:
        raise RuntimeError("Matrix must be square to calculate determinant")

    if rows == 1:
        return mtx[0][0]

    if rows == 2:
        return mtx[0][0] * mtx[1][1] - mtx[0][1] * mtx[1][0]

    det = 0
    for j in range(cols):
        det +=mtx[0][j] * cofactor(mtx, 0, j)
    return det

# Cofactor function -> minor multiplied by the sign (-1)^(i+j)

def cofactor(mtx, i, j):
    sign = (-1) ** (i+j)
    return sign * determinant(minor(mtx, i, j))

#Inverse function -> Adjugate divided by determinant

def inverse(mtx):
    det = determinant(mtx)

    if det == 0:
        raise RuntimeError('Matrix is not invertable (determinant is 0)')

    rows, cols = size(mtx)
    cofactor_matrix = [[cofactor(mtx, i, j) for j in range(cols)] for i in range(rows)]
    adjugate = trans(cofactor_matrix)
    return [[adjugate[i][j] / det for j in range(cols)] for i in range(rows)]


#MATRICES
A = [
    [1,2,3],
    [1,0,0],
    [7,8,9]
]

B = [
    [2,1],
    [3,4],
    [1,0]
]

C = [
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [1,0,1,0]
]

D = [
    [0,1,2],
    [1,2,3]
]

E = [
    [0,0,1],
    [0,1,1]
]

#TESTING

print(generate(3,3))
print(scalar_mul(3,A))
print(scalar_add(3,A))
print(mul(A,B))
#print(mul(A,C)) # cannot multiply
print(concat(E,D))
#print(concat(A,B)) # cannot concat
print(add(E,D))
#print(add(A,B)) #cannot add
print(sub(E,D))
#print(sub(A,B)) #cannot subtract
print(sum_el(A))
print(prod_el(A))
print(trans(A))
print(identity(C))
print(minor(C, 0, 0))
print(determinant(A))
print(cofactor(A, 0, 0))
print(inverse(A))



