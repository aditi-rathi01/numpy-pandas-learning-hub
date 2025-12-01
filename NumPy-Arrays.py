
# ======= Learning NumPy Arrays ===========


# If we want to save 100 students subject marks, we need to make 100 variables like m1, m2, m3...., but with the use of array we can 
# store it in one variable.

# NOTE :
# Arrays are similar to lists. The main difference is that arrays can store only one type of elements; where as lists can store 
# different types of elements, array uses less memory than lists. and arrays are faster, then list


# --- CREATING ARRAYS USING array()---


import numpy as np
arr = np.array([10,20,30,40,50])     # This is a method to create a array, where we use np in place of numpy
print(arr)

from numpy import *
ar = array([5,15,25,35,45,55])     # This is also a method to create a array, Here we use *. so, we don't need to write numpy and np
print(ar)

Arr = array([12,55,23.7, 45, 78.23])   # Python will convert all int type elements into float type. hence, all elements are uniform

arr = array(["aditi", "shivam", "rathi","python"])
print(arr)

# WAP to create an array from an array 
a = array([2,4,6,8,10])
b = array(a)
c = a 

# --- CREATING ARRAY USING linespace ----

# program 1: creating an array using linespace with 5 equal points.

arra = linspace(0,10,5)   
print(arra)

# --- CREATING ARRAY USING logspace ---

# program 1: WAP to create an array using logspace().

# divide the range: 10 power to 10 power 4 into 5 points and take those points in array.

a = logspace(1,4,5)
print(a)

# --- CREATING ARRAY USING arrange() function.

# program 9: WAP to create an array with even number up to 10.

c = arange(2,11,2)
print(c)

# --- MATHEMATICAL OPREATIONS on arrays---

arr1 = array([10,44,23,45,20])          # Here, we don't use any np and something else. because we already apply (*)this.
arr1 =  arr1+10                 # Adding 10, in every element of array.
print(arr1)


arr2 = array([5,10,5,23,66])
arr3 = arr2 - arr1   
print(arr3)

# //  all mathematical opreations on arrays.

print(sum(arr1))
print(max(arr1))
print(min(arr1))
print(mean(arr1))
print(sin(arr1))


# --- INDEXING AND SLICING in numpy arrays ---

# Indexing: indexing refers to location of the elements.
# Slicing: slicing refers to extracting a range of elements.

# Program 1: WAP to retrieve and display elements of a numpy array using indexing.

arr4 = array([10,20,30,40,50,65,87])
print(arr4[1:7])

# display elements using indexig.
for i in range(len(arr4)):
    print(arr4[i])

# // slicing 

print(arr4[1:7:3])
