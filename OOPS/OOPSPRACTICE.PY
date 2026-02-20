# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#     def student_details(self):
#         print(f" student name is : =({self.name}) and his grade is := [{self.grade +2} %]")

# student1=Student("preetam",90)
# print(student1.name,student1.grade)
# student2=Student("ganesh", 80)

# print(student2.name,student2.grade)

# student1.student_details()
# student2.student_details()

# class GradStudent(Student):
#     def __init__(self,name,grade,stream):
#         super().__init__(name,grade)
#         self.stream=stream
#     def student_details(self):
#             super().student_details()
#             print(f"name is {self.name},grade is {self.grade} and stream is {self.stream}")

# GradStudent1=GradStudent("reddy",99,"pcm")
# print(GradStudent1.name,GradStudent1.grade,GradStudent1.stream)
# print(GradStudent1.student_details())



class Car:
    def __init__(self):
        self.exltor=True
        self.cluch=True
        self.brek=False
    
    def start(self):
        self.exltor=True
        self.cluch=True
        print("car started")

    car1=Car()
    car1.start()
