#to find the number is perfect number or not
n=int(input("enter a number:"))
sum=0
for i in range (1,n):
	if(n%i==0):
		sum+=i
print(sum)
if(n==sum):
	print("The given number is a perfect number")
else:
	print("The given number is not a perfect number")
