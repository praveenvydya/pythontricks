""" 1. Stacking and Splitting Arrays """

import numpy as np

# Vertical and horizontal stacking
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vstack = np.vstack((a, b))
print("Vertical Stack:\n", vstack)

hstack = np.hstack((a, b))
print("Horizontal Stack:", hstack)

# Splitting arrays
c = np.array([10, 20, 30, 40, 50, 60])
split = np.split(c, 3)
print("Split Array:", split)

#-------------------------------------------
""" 2. Advanced Indexing """

# Integer array indexing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = [0, 2]  # Select rows 0 and 2
print(arr)
print("Selected Rows:\n", arr[indices])

# Boolean indexing
mask = arr > 5
print("Boolean Mask:\n", mask)  # double check returns 3x3 array of boolean
print("Filtered Elements:", arr[mask])

# Fancy indexing
rows = np.array([0, 1, 2])
cols = np.array([2, 1, 0])
print("Fancy Indexed Elements:", arr[rows, cols]) # (row 0,col 2) , (row1,col1), (row2,col0)

#------------------------------------------------

"""  3. Linear Algebra Operations  """

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])

product = np.dot(A, B)
print("Matrix Product:\n", product)

# Determinant
det = np.linalg.det(A)
print("Determinant:", det) # a.d-b.c

# Eigenvalues and Eigenvectors
eigvals, eigvecs = np.linalg.eig(A)  #det(A−λI)=0
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)

# Solving linear systems (Ax = b)
b = np.array([5, 11])
x = np.linalg.solve(A, b)
print("Solution to Ax = b:", x)
#------------------------------------------
""" Broadcasting with Multi-dimensional Arrays """

# Broadcasting in higher dimensions
X = np.array([[1, 2, 3], [4, 5, 6]])
Y = np.array([1, 2, 3])

result = X * Y  # Element-wise multiplication
print("Broadcasted Multiplication:\n", result)

#-----------------------------------------

""" Random Number Generation """

# Random numbers
random_array = np.random.rand(3, 3)  # Uniform [0, 1)
print("Random Array:\n", random_array)

# Random integers
random_ints = np.random.randint(0, 10, (3, 3))  # Integers in [0, 10)
print("Random Integers:\n", random_ints)

# Normal distribution
normal_array = np.random.randn(3, 3)  # Mean 0, Std. Dev. 1
print("Normal Distribution:\n", normal_array)

# Set random seed for reproducibility
np.random.seed(42)
print("Reproducible Random Array:\n", np.random.rand(3, 3)) # Always  same fixed matrix

#-----------------------------------------------
""" Advanced Reshaping with np.ravel and np.flatten """

# Flattening a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
ravelled = matrix.ravel()  # View of the array
flattened = matrix.flatten()  # Copy of the array

print("Ravelled Array:", ravelled)
print("Flattened Array:", flattened)

"""
np.ravel():

Returns a view of the array, not a copy. This means any modifications to the ravelled array will also affect the original matrix (if possible, depending on the memory layout).
It is more memory-efficient since it avoids creating a new array unless necessary.

np.flatten():

Returns a copy of the array, which means changes to the flattened array will not affect the original matrix.
It always creates a new array in memory, consuming more resources compared to ravel().

"""
#Memory View vs. Copy: If you modify ravelled, it affects matrix (if allowed), but modifying flattened does not.
ravelled[0]=10
print(matrix)
flattened[1]=9
print(matrix)
#Use ravel() when you want a lightweight, memory-efficient view of the original array and might modify it.
#Use flatten() when you need an independent copy of the array and want to ensure the original remains unchanged.
#-----------------------------------------------
"""  Statistical Operations Across Axes  """

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

# Mean across rows
row_mean = np.mean(arr, axis=1)
print("Row Mean:", row_mean)

# Sum across columns
col_sum = np.sum(arr, axis=0)
print("Column Sum:", col_sum)

# Sum across rows
row_sum = np.sum(arr, axis=1)
print("Row Sum:", row_sum)

# Standard deviation across rows
row_std = np.std(arr, axis=1)
print("Row Standard Deviation:", row_std)
#----------------------------------------------

""" Using np.where for Conditional Operations """
arr = np.array([10, 15, 20, 25, 30])

# Replace elements based on a condition
modified_arr = np.where(arr > 20, -1, arr)
print("Modified Array:", modified_arr)

# Find indices of elements satisfying a condition
indices = np.where(arr > 15)
print("Indices of Elements > 15:", indices)

#----------------------------------------------

"""  Custom Universal Functions (ufuncs) """
# Creating a custom ufunc
def custom_function(x):
    return x**2 + 2*x + 1

u_func = np.frompyfunc(custom_function, 1, 1)  # 1 input, 1 output
arr = np.array([1, 2, 3, 4])
result = u_func(arr)
print("Result of Custom Ufunc:", result)

#--------------------------------------------
""" Memory and Efficiency """
# Memory usage comparison
arr = np.arange(1e6)
print("Size of NumPy Array (bytes):", arr.nbytes)

# Using views for memory-efficient slicing
matrix = np.arange(9).reshape(3,3)
view = matrix[:, :2]
print(view) # first two rows
view[0, 0] = 99  # This change affects the original array
print("Modified Original Array:\n", matrix)
#-----------------------------------------------


