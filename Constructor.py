class Constructor:
	def __init__(self,fn,ln):
		self.firstnum=fn
		self.secondnum=ln
	def display(self):
		print("First num=",self.firstnum)
		print("Second num=",self.secondnum)
		print("sum of two numbers=",self.firstnum+self.secondnum)
a=Constructor(11,19)
a.display()


