import numpy as np

arr1 = np.array(list(map(int, input("\nEnter elements of Array 1 \n").split())))

arr2 = np.array(list(map(int, input("\nEnter elements of Array 2\n ").split())))

print("\nArray 1:", arr1)
print("\nArray 2:", arr2)

add = arr1 + arr2
print("\nAddition:", add)

mul = arr1 * arr2
print("\nMultiplication:", mul)

mean = np.mean(arr1)
var = np.var(arr1)
sd = np.std(arr1)

print("\nMean of arr1:", mean)
print("\nVariance of arr1:", var)
print("\nStandard Deviation of arr1:", sd)
