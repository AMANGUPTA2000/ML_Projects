import numpy as nm
arr=nm.array([[1,2,3,4],[3,4,5,6],[6,7,8,9],[9,0,1,2]])
arr1 = nm.split(arr,4)
arr2 = nm.concatenate(arr1)
arr2 = arr2.ravel() #for linear 1d array
print("Before Indexing: ",arr2)
arr3 = nm.empty(0, dtype=object) #creating empty array
print("After even Indexing (0 as first index): ")
for i in range(0, len(arr2), 2):
    arr3 = nm.append(arr3,arr2[i])
print(arr3)
