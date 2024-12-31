import numpy as np
"""
Key Advantages of Using NumPy
1. Performance: NumPy arrays are faster than Python's array.array due to their optimized C implementation.
2. Flexibility: NumPy supports multidimensional arrays and a vast array of mathematical operations.
3. Broadcasting: You can perform element-wise operations directly.
4. Rich Ecosystem: NumPy integrates seamlessly with libraries like Pandas, Matplotlib, and SciPy.

"""

arr = np.array([0, 18446744073709551615], dtype=np.uint64)
print(arr)  # [                   0 18446744073709551615]
print(arr.dtype)

#For example, operations like multiplication can be done element-wise:

arr = np.array([1, 2, 3], dtype=np.int8)
print(arr * 2)  # [2 4 6]
print(arr**3)


"""
when to Choose NumPy over array.array?
Use NumPy whenever:

You need advanced numerical operations.
You are working with multidimensional data.
Performance and scalability are priorities.
For basic one-dimensional arrays where you need type constraints, array.array can suffice, but NumPy provides far more functionality for modern applications.

"""
# 1. Array Creation and operations
# Create Arrays with Specific Patterns
zeros = np.zeros((3, 3))
print(zeros)

ones = np.ones((2, 4)) # 2 rows of 4 columns of ones
print(ones)

## Create a range of numbers
a_range = np.arange(0, 10, 2)
print(a_range)
print([x for x in range(0,10,2)])

# Create an evenly spaced array
linspace = np.linspace(0, 1, 5)
print(linspace)

# Create a random array
random_array = np.random.random((2, 3))
print(random_array)

# Basic arithmetic
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Element-wise operations
print("Square of elements:", a ** 2)

# Mathematical functions
print("Sin of elements:", np.sin(a))
print("Exponential of elements:", np.exp(a))



""" 2. Array Indexing and Slicing  """
arrx = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access a specific element
print(arrx[1, 2])  # 6

# Slice rows and columns
print(arrx[:, 1])  # [2, 5, 8] (second column)

# Modify elements
arrx[0, 0] = 99
print(arrx)

# Accessing elements
arr = np.array([10, 20, 30, 40, 50])
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("Slice 1 to 3:", arr[1:4])

# Access elements in a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at (1, 2):", matrix[1, 2])  # Row 1, Column 2
print("First row:", matrix[0])
print("Second column:", matrix[:, 1])

"""  
3. Broadcasting and Vectorized Operations
Perform Element-Wise Operations Without Loops """
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Element-wise addition
print(x + y)

# Element-wise multiplication
print(x * y)
print(x*arrx)

""" 
4. Boolean Masking
Filter Data Using Conditions
"""

data = np.array([10, 20, 30, 40, 50])

# Find elements greater than 25
mask = data > 25
print(data[mask])  # [30, 40, 50]

# Replace values
data[data > 25] = 100
print(data)

d = np.array([1,0,1,0,1,0,1,0,0,1])
d[d==0] =9
print(d)

# Adding a scalar to an array
arr = np.array([1, 2, 3])
print("Array + 10:", arr + 10)

# Broadcasting in operations
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, -1])
print("Matrix + Vector:\n", matrix + vector)


#--------------------------------------
"""
Array Reshaping and Transposing
"""
arr = np.arange(1,10)
reshaped = arr.reshape(3,3)

print("Reshaped Array:\n", reshaped)

# Transpose
print("Transpose:\n", reshaped.T)

"""
7. Aggregations
"""

arr = np.array([1, 2, 3, 4, 5])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Standard Deviation:", np.std(arr))























