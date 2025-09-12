#to print fibonacci series
a=0
b=1
n=int(input("enter no.of fibonacci series order:"))
for i in range(n):
	print(a,"",end="")
	a,b=b,a+b
	
