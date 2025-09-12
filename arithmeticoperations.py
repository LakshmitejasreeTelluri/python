def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	if b==0:
		return "error"
	else:
		return a/b
x=int(input("enter first number:"))
y=int(input("enter second number:"))
print("Addition",add(x,y))
print("Subtraction",subtract(x,y))
print("Multiplication",multiply(x,y))
print("Division",divide(x,y))
