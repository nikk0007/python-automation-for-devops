import numpy as np

# Create a 1-dimensional NumPy array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Create a 2-dimensional NumPy array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)

# Perform basic operations on NumPy arrays
print(arr1 + 1)       # Add 1 to each element
print(arr1 * 2)       # Multiply each element by 2
print(arr1 ** 2)      # Square each element

# Accessing elements in NumPy arrays
print(arr1[2])        # Access element at index 2
print(arr2[1, 2])     # Access element at row 1, column 2

# Perform mathematical operations on NumPy arrays
print(np.sum(arr1))             # Sum of all elements
print(np.mean(arr2))            # Mean of all elements
print(np.max(arr1))             # Maximum element
print(np.min(arr2, axis=0))     # Minimum element along each column
print(np.std(arr2, axis=1))     # Standard deviation along each row
