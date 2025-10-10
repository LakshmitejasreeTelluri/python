#interchanging the first and last elements in the list
l=[]
n=int(input("Enter size of list:"))
for i in range(n):
	ele=int(input("Enter elements into list:"))
	l.append(ele)
print("List:",l)
l[0],l[n-1]=l[n-1],l[0]
print("After interchanging the first and last elements the list is ",l)
