import numpy as nm
arr=nm.array([[1,2,3,4],[3,4,5,6],[6,7,8,9],[9,0,1,2]])
print(arr)
arr_diagonal_element = arr.diagonal()
print("\nDiagonal element:",arr_diagonal_element)
print("\nSum of Diagonal elements:",nm.sum(arr_diagonal_element))
