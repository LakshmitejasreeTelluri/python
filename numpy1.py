import numpy as np
arr=np.arange(1,20,3)
print("Original array:",arr)
print("Printing elements of 2 to 5 indexes using Slicing:",arr[2:6])
print("Jumping to next number using slicing:",arr[2:6:1])
print("Jumping to second number using slicing:",arr[2:6:2])
print("Jumping to third number using slicing:",arr[2:6:3])
print("Integer indexing:",arr[[5,3,0,2,1]])#numbers will be printed according to their index
print("Boolean indexing:",arr[arr>11])#numbers greater than 11 will be printed in the output

