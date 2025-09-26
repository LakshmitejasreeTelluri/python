class Student:
	branch="CSE"
	def read_student_details(self,rno,n):
		self.__rollno=rno
		self.name=n
	def print_student_details(self):
		print("Student rollno is",self.__rollno)
		print("student name is:",self.name)
		print("student branch is:",Student.branch)
s=Student()
s.read_student_details("24PA1A05M8","TEJA")
s.print_student_details()
print(s.name)
print(s.__rollno)
