class student:
    def __init__(self,name,age,garde):
        self.name=name
        self.age=age
        self.grade=garde
    def student_details(self):
        print(f"student name is {self.name} \n student age is {self.age+1} \n \t and student grade is {self.grade} ")

student1=student("preeatam",23,"A+")
student2=student("ganesh",24,"A")
student3=student("ankita",22,"B+")

class gradstudent (student):
    def __init__(self,name,age,grade,percent):
        super().__init__(name,age,grade)
        self.percent=percent
    def student_details(self):
         super().student_details()
grad_stu1=gradstudent("abhishek",25,"A",91)
grad_stu2=gradstudent("veeresh",21,"C",65)
grad_stu1.student_details()
student1.student_details()
# print(grad_stu1.percent)

