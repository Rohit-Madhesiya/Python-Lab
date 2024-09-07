import numpy as np

# Create an array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Type of array
arr_type = type(arr)
print("Type:",arr_type)

# Axes of array
arr_axes = arr.ndim
print("Axes:", arr_axes)

# Shape of array
arr_shape = arr.shape
print("Shape:", arr_shape)

# Type of elements in array
arr_dtype = arr.dtype
print("Data Type:",arr_dtype)
