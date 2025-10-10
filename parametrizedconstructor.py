class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return self.length*self.breadth
r1=Rectangle(11,19)
print("Rectangle1:")
print("Area:",r1.area())
