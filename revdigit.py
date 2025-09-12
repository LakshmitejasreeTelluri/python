n=int(input("Enter a number:"))
rev=0
while(n>0):
	k=n%10
	rev=rev*10+k
	n=n//10
print("the number after reversing digits is:",rev)
