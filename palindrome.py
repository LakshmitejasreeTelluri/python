#to check whether the given number is palindrome or not
n=int(input("Enter a number:"))
temp=n
rev=0
while(n>0):
	k=n%10
	rev=rev*10+k
	n=n//10
print("the number after reversing digits is:",rev)
if(temp==rev):
	print("the given number is palindrome")
else:
	print("The given number is not a palindrome")
