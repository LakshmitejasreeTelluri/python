def gcd(a,b):
	if b==0:
		return "error"
	while b:
		a,b=b,a%b
	return a
x=int(input("Enter Dividend:"))
y=int(input("Enter Divisor:"))
print("GCD of",x,"and",y,"is:",gcd(x,y))
