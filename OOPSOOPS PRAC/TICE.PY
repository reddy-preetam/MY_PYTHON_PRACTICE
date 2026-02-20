UMXD class student:
    def __init__(self,name,age,garde):
        self.name=name
        self.age=age
        self.grade=garde
    def student_details(self):
        print(f"student name is {self.name} \n student age is {self.age} \n \t and student grade is {self.grade} ")

student1=student("preeatam",23,"A+")
student2=student("ganesh",24,"A")
student3=student("subhash",22,"B+")
print(student1.age)
student1.student_details()
student2.student_details()
student3.student_details()
print(student2.age,student1.name,student3.grade)

