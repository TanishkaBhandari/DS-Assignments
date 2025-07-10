import numpy as np 

#CHECK IF NUMBER IS PRIME
fac=0
print("CHECK IF NUMBER IS PRIME")
n=int(input("Enter a number "))
for i in range(2, n):
	if(n%i==0):
		fac+=1
if(fac==0):
		print("IT IS A PRIME NUMBER")
else:
		print("IT IS NOT A PRIME NUMBER")
print("/n")

#CALCULATE FACTORIAL OF A NUMBER
print("CALCULATE FACTORIAL OF A NUMBER")
fact=1
n=int(input('Enter number '))
for i in range(n, 0, -1):  
    fact *= i

print("\nFACTORIAL OF THE NUMBER =", fact)


#TRANSPOSE MATRIX
mx=np.array([[1,2,3],[9,0,4]])
print(np.transpose(mx))

#LINEAR SEARCH ON ARRAY
import numpy as np
arr=np.array([1,7,8])
x = int(input("Enter element to search: "))
flag = 0

for i in range(len(arr)):  
    if x == arr[i]:
        flag = 1
        break

if flag == 1:
    print("\nElement found at location", i + 1)
else:
    print("\nElement not found in array")

#BINARY SEARCH
num = int(input("Enter element to search: "))

a = np.array([2, 4, 7, 10, 15, 20]) 
l = 0
h = len(a) - 1
flag2 = 0

while l <= h:
    mid = (l + h) // 2

    if num == a[mid]:
        flag2 = 1
        break

    if num > a[mid]:
        l = mid + 1
    else:
        h = mid - 1

if flag2 == 1:
    print("Element found at position", mid + 1)
else:
    print("Element not found")





	
