import numpy as np

arr1 = np.array([5, 10, 15, 20, 25])
arr2 = np.array([50, 250, 330, 410, 510])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Element-wise addition
add_result = arr1 + arr2
print("\n Addition:", add_result)

# Element-wise multiplication
mul_result = arr1 * arr2
print("Multiplication:", mul_result)

# Compute statistics
mean_val = np.mean(arr1)
var_val = np.var(arr1)
std_val = np.std(arr1)

print("\nMean of arr1:", mean_val)
print("Variance of arr1:", var_val)
print("Standard Deviation of arr1:", std_val)