#to find no.of vowels in a string
str='Hello VIT'
count=0
total=0
l=['a','e','i','o','u','A','E','I','O','U']
for i in str:
	if(i in l):
		count+=1
		print(i)
	else:
		total+=1
		print(i)
print("the no.of vowels in string:",count)
print("the no.of consonants in string:",total)
