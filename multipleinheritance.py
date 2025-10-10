class Person:
	def show_person(self):
		print("This is person class")
class Student:
	def show_student(self):
		print("This is student class")
class Teacher(Person,Student):
	def show_Teacher(self):
		print("This is Teacher class")
t=Teacher()
t.show_person()
t.show_student()
t.show_Teacher()

