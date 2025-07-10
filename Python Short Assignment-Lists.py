#MERGE 2 SORTED LISTS
print('MERGE 2 SORTED LISTS')
a=[]
b=[]
s=[]

for _ in range(5):
    a.append(int(input('Enter next value for list a ')))
for _ in range(5):
    b.append(int(input('Enter next value for list b ')))
a.sort()
b.sort()
i=0
j=0
while i<(len(a)) and j<(len(b)):
        if a[i] < b[j]:
            s.append(a[i])
            i += 1
        else:
            s.append(b[j])
            j += 1
            
s.extend(a[i:])
s.extend(b[j:])

print('Sorted merged list is ',s)
print("\n")



#REMOVE DUPLICATES FROM A LIST
print("REMOVE DUPLICATES FROM A LIST")
l=[]
for i in range(5):
    l.append(int(input('Enter next value for list l ')))
print(l)
i = 0
while i < len(l):
    if l.count(l[i]) > 1:
        l.remove(l[i])  # removes first match
    else:
        i += 1

print('List with duplicates removed ',l)
print("\n")

#FIND THE 2ND LARGEST NUMBER IN A LIST
print("#FIND THE 2ND LARGEST NUMBER IN A LIST")
lg=0
j=0
for j in range(len(l)):
     if l[j]>lg:
          lg=l[j]
print('Largest number in list is ',lg)
l.sort()
lg=l[-1]
lg2=0
for i in range(len(l)):
     if l[i]<lg and l[i]>l[i-1]:
          lg2=l[i]
print('Second Largest number in list is ',lg2)

#COUNT OCCURENCES OF ELEMENTS IN A LIST
print("\n")
print("#COUNT OCCURENCES OF ELEMENTS IN A LIST")
ct = []
for x in l:
    if x not in ct:
        print(f"{x} occurences {l.count(x)}")
        ct.append(x)
print("\n")

#MOVING ALL ZEROES IN LIST TO THE END
print("MOVING ALL ZEROES IN LIST TO THE END")
for t in range(len(l)):
    if l[t]==0:
        z = l.pop(t)
        l.append(z)   
print(l)

#CHECK IF A LIST IS SORTED
print("CHECK IF A LIST IS SORTED")
lt=[]
length=int(input("How many elements do you want in your list? "))
for y in range(length):
    lt.append(int(input('Enter next value for list ')))
print(lt)
if lt==sorted(lt):
    print("List is sorted!")
else:
    print("List is not sorted :(")

