#to print the string with even length
str='I am Laxmi'
l=str.split()
print(l)
for i in l:
	if(len(i)%2==0):
		print("the string with even length:",i)
	i+=i
