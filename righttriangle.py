#to print stars in right angle triangle shape
n=int(input("Enter no.of rows:"))
for i in range (n+1):
	for j in range (1,i+1):
		print('*',"",end="")
	print("")
