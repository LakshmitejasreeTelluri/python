n=int(input("Enter a number:"))
sum=0
for i in range(1,n):
	k=n%10
	sum+=k
	n=n//10
print("the sum of digits of a number is:",sum)
