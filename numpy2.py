import numpy as np
arr1=np.array([11,19,5,20,25,4])
arr2=np.arange(1,12,2)
print("array 1:",arr1)
print("array 2",arr2)
#arthemetic operations
print("Sum of Arrays:",arr1+arr2)
print("Difference of Arrays:",arr1-arr2)
print("Product of Arrays:",arr1*arr2)
print("Division of Arrays:",arr1/arr2)
print("Modulus of Arrays:",arr1%arr2)
print("Exponent of Arrays:",arr1**arr2)
#statastical operations
print("Minimum element in array1:",arr1.min())
print("Maximum element in array1:",arr1.max())
print("Sum of elements in array1:",arr1.sum())
print("Cumulative sum of elements in array1:",arr1.cumsum())
print("Mean of elements in array1:",arr1.mean())
