list=[]
a=int(input("Enter number of elements:"))

for i in range(1,a+1):
    b=int(input("Enter element:"))
    list.append(b)
even=[]
odd=[]
for j in list:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)

print("The list is",list)        
print("The even list",even)
print("The odd list",odd)
