#to check whether the given string is palidrome or not
str='malayalam'
temp=str
rev_str=''
for i in str:
	rev_str=i+rev_str
print("reversed string:",rev_str)
if(temp==rev_str):
	print(str,"is a palindrome")
else:
	print(str,"is not a palindrome")
