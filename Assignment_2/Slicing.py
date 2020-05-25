import numpy as nm
arr=nm.array([[1,2,3,4],[3,4,5,6],[6,7,8,9],[9,0,1,2]])
print("Before Slicing:\n",arr)
arr1 = nm.split(arr,4)
print("After Slicing:",arr1)
