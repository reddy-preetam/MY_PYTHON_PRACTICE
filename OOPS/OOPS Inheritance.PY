#Inheritance :== allow on class (child to reuse the property nad methods of another 
#class(parent)

#parent classs:-
class student:
    def __init__(self,name,grade,percentage):# Method
        self.name=name #attribute
        self.grade=grade 
        self.percentage=percentage 

    def student_details(self):
        print(f"{self.name} is in class {self.grade} with {self.percentage+2} % ") #hidden from user
  
#Object==instance of class....

student1=student("preeatm",11,96)
student2=student("rishab",12,95)

#child class:--

class graduatestudent(student):#graduate student is child calss 
    #inherit property and methods from student parent cllass

    def __init__(self,name,grade,percentage,stream):#parameter from old parent class
        #and new parameters in child class 

        super().__init__(name,grade,percentage) #call parent class __init
        self.stream=stream #new atribute from child class

    def student_details(self):
        super().student_details() #method inheritate from parent class

grad_student=graduatestudent("preetam",12,92,"PCM")
grad_student.student_details()
# print(grad_student.stream)

