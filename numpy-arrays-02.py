# --- Numpy Arrays part(2.0) ---



# ====  Dimensions of Arrays =====
# 
#   // 1-D Array
# A 1D array is a single list of element.


# // 2-D Array 
# A 2D array look like rows and columns.

# // 3-D
# A 3D array is collection of data arranged in three dimensions: layers(also called depth), rows and colunms.



# Create a  1-D Array:
from numpy import *

arr1 = array([12,24,36,48,60])


# Create a 2-D Array:

arr2 = array([[12,24,36,48],
              [13,26,39,52]])


# Create a 3-D Array:

arr3 = array([[[2,4,6,8],[3,6,9,1]],
              [[4,8,12,16],[5,10,15,20]]])



# ==== Attributes of an Array ====

# An Attributes represents properties of array.


# // The ndim Attribute 
# ndim Attributes represent dimensions or axis of array.
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)


#// The shape attribute
# The 'shape' attribute gives the shape of array. we can also change the shape of array using 'shape' attributes.

print(arr1.shape)
print(arr2.shape)
print(arr3.shape)

# In arr2 there are 2 rows and 3 columns. we can change rows to column and column to rows using shape attribute.

arr2.shape = (4,2)
print(arr2.shape)
print(arr2)

# // The size Attribute.

print(arr1.size)
print(arr2.size)
print(arr3.size)

# // The itemsize Attribute
# The 'itemsize' attribute gives the memory size of the array element in bytes. Generally, int64 and float64 takes 8 bytes memory.

print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)

# // The dtype Attribute
# the 'dtype' attribute gives the datatype of the element in the array.

print(arr2.dtype)

# // The nbytes Attribute
# The 'nbytes' attributes gives the total number of bytes occupied by an array.
# The total of bytes = size of the array* item size of each element.

print(arr1.nbytes)
print(arr2.nbytes)
print(arr3.nbytes) 

# Note: In old version of NumPy(many years ago) int type take 4 bytes in memory and float take 8 bytes in memory.


# ==== The reshape() Method ====
# The 'reshape()' method is useful to change the shape of an array. The new array should have same number of element as in the old
# array.

arr4 = array([1,2,3,4,5,6,7,7,8,0])
print(arr4.reshape(2,5))
print(arr4.reshape(5,2))


# === The flatten() Method ===
# The flatten() method is useful to convert 2-D Array into 1-D Array.

arr2 = arr2.flatten()
print(arr2)