
# #Abstration ==hiding unnecessary  details from users  through class and methods...
# class student:
#     def __init__(self,name,grade,percentage):# Method
#         self.name=name #attribute
#         self.grade=grade #attribute
#         self.percentage=percentage #attribute
#     def student_details(self):#method abstarction
#         print(f"{self.name} is in class {self.grade} with {self.percentage+2} % ") #+2 its hiddin by user     
  
# #Object==instance of class....

# student1=student("RAVI",11,96)
# student2=student("rishab",12,95)
# student1.student_details()
# student2.student_details()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Person_details (self):
        print(f"student name{self.name} and is age is {self.age+1}")
    
Person1=Person("reddy",23)
print(Person1.age)
    
    
   
   
