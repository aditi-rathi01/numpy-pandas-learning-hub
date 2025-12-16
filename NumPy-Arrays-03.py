# ----- Working with Multi-dimensional arrays.  ------


# As In mathematics, matrix contains elements arranged in several rows and columns. Hence, we can take a matrix as 2D array 
# and vice versa. we can create multi-dimensionals arrays in the following ways.

# - Using array() function.
# - Using ones() and zeros() fuctions.
# - Using eye() function.
# - Using reshape() function.

# ======= The array() Function: =======

from numpy import *
a = array([2,4,6,8,10])   # Creates 1-D Array
print(a)

a2 = array([[1,2,3,4], [5,6,7,8]])   # Creates a 2D Array.
print(a2)

# Here, a2 = 
#     +-----+-----+------+-----+-----+------+-----+-----+
#     |  1  |  2  |  3   |  4  |  5  |  6   |  7  |  8  |          \\ Elements
#     +-----+-----+------+-----+-----+------+-----+-----+
#     [0][0] [0][1] [0][2]...   [1][0] [1][1]...   [1][3]           \\ Index


#  ====== The ones() and zeros() Functions ======

# The ones() fuction is useful to create a 2D array where all the elements of array is one. The format of the function is:

# // ones((r,c), dtype)

b = ones((4,5), int)
print(b)

# In the same format, we can use zeros() Function.

b2 = zeros((6,3), float)
print(b2)

# ====== The eye() function =======

# Create 2D arrays where all the elements are zero. except diagonal elements. where, diagonal elements are one. The format is

# // eye(n, dtype = datatype)
c = eye(4)
print(c)   # default datatype is float.



# ==== Indexing and slicing in Multi-diminsional ====

# Index represent the location number.
# a[0][1]  represents 0th row and 1st column element in the array.

# Here, let a 2D array is given 'a5'. so len(a5) gives no. of rows. and len(a5[i]) gives the number of columns.

a5 = array([[1,2,3], [4,5,6],[7,8,9]])
print(a5)
for i in range(len(a5)):
    for j in range(len(a5[i])):
        print(a5[i][j],end=" ")


# Program 1: WAP to retrieve the elements from a 3D array.

# create a 3D array.
a7 = array([[[1,2,3],
             [4,5,6]],
       
             [[7,8,9],
             [10,11,12]]])
print(a7)
# display element by element
for i in range(len(a7)):
    for j in range(len(a7[i])):
        for k in range(len(a7[i][j])):
            print(a7[i][j][k],end=" ")


# ===== The reshape() Function =====

# reshape() is a NumPy function that changes the shape of an existing array without changing its data.

a8 = array([1,2,3,4,5,6,7,8])
b3 = a8.reshape(2,4)
print(b3)


# ==== The arange() Function =====

a9 = arange(1,20,3)
print(a9)

# ===== Slicing Multi-dimensional Arrays.=====

a10 = reshape(arange(11,36,1),(5,5))       # Gives a matrix in which there are 5 rows and 5 columns.
print(a10)

# Retrieve 0th row from the array.
print(a10[0])   # and also
print(a10[0,:]) 
# Another, method
for i in range(5):
    print(a10[0][j], end=" ")
print("/n")


# Retrieve all rows with 1st column.
for j in range(5):
    print(a10[j][1], end=" ")             # Method one.
print("/n")

# Method two
print(a10[0:5,1:2])

# program 1: Retrieve 0th row to 1st with column from 0th column to 2nd column.

# Method one
print(a10[0:2, 0:3])

# Method Two
for i in range(2):
    for j in range(3):
        print(a10[i][j], end=" ")
    print()


# program 2: To Retrieve 2nd and 3rd rows with 3 columns and 4th columns.

# Method 1:
print(a10[2:4,3:5])

# Method 2
for i in range(2,4):
    print("[", end=" ")
    for j in range(3,5):
        print(a10[i][j], end=" ")
    print("]")
        

# Matrices in Numpy


# Method one

a11 = [[1,2,3],[4,5,6]]
m = matrix(a11)
print(m)

# Matrices are also made from string
str1 = "1  2 ; 3 4 ; 5 6 "            # Observe the semicolon after each row of elements
m1 = matrix(str1)
print(m1)

# Getting diagonal elements of a matrix

# // To retrieve the diagonals elements of a matrix, we can use diagonal function as:
# a = diagnoal(matrix)

a13 = matrix([[12,24,36],[13,26,39]])
print(a13)

d = diagonal(a13)
print(d)

# Finding maximum and minimun elements

# To find maximun and minimum elements. we use max() and min() methods respectively.
print(a13.max())
print(a13.min())

# Finding sum and averages of the elements.

print(a13.sum())
print(a13.mean())

# Products of elements.
m2 = matrix(arange(12).reshape(3,4))
print(m2)

# To find the product of element column wise, we can call prod(0), and for row wise product, prod(1)
print(m2.prod(0))
print(m2.prod(1))

# Transpose the matrix
str2 = "1 2 3 ; 4 5 6 ; 7 8 9 "
m3 = matrix(str2)
print(m3)
print(m3.transpose())

# Another method to get transpose of matrix is
print(m3.getT())


# program: A pyhton program to accept a matrix from the keyboard and display its transpose matrix.

r , c =  [int(a) for a in input("enter rows and columns:").split()]

# Accepting matrix elements as a string.

str3 = input("Enter matrix elements:\n")

x = reshape(matrix(str3), (r,c))
print("the original matrix is :")
print(x)

print("the transpose of matrix is:")
print(x.transpose())

# Matrix Addition and multiplication

# we can use arthemetic opreations like addition, subtraction and division on the matrices.

a = matrix("1 2 3; 4 5 6")
b = matrix("2 4 6; 3 6 9")
c = a + b 
print(c)

# Note :- Here, * opreator to perfom matrix multiplication. this does not multiply corresponding elements of matrices.

 
