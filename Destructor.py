class Destructor:
	def __init__(self):
		self.greet="Hi,have a nice day"
	def display(self):
		print("Msg:",self.greet)
	def __del__(self):
		print("The object is destroyed")
d=Destructor()
d.display()
del d
