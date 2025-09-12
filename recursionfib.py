def rfib(n):
	if n<=1:
		return n
	else:
		return rfib(n-1)+rfib(n-2)
n=int(input("enter no.of terms:"))
l=[]
for i in range(n):
	l.append(rfib(i))
print(l)

