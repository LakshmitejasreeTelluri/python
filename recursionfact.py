def rfact(n):
	if n==0:
		return 1
	else:
		return n*rfact(n-1)
n=int(input("enter n value:"))
if n<0:
	print("factroial not exist")
else:
	print("the factroial of",n,"is:",rfact(n))
