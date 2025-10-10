class Parent:
	def fun1(self):
		print("This is fun1")
class Child1(Parent):
	def fun2(self):
		print("This is fun2")
class Child2(Child1):
	def fun3(self):
		print("This is fun3")
ob=Child2()
ob.fun1()
ob.fun2()
ob.fun3()
