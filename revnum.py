n=int(input("Enter a number:"))
rev=0
for i in range n:
	k=n%10
	rev=rev*10+k
	n=n//10
print("the reveresed number is:",rev)
