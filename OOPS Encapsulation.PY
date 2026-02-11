class student:
    def __init__(self,name,grade,percentage):# Method
        self.__name=name #attribute
        self.grade=grade 
        self.__percentage=percentage #dounble underscore limit acess
    def get_name(self):
        return self.__name

    def get_percentage(self): # Encapsulation method
        return self.__percentage 
    
    def student_details(self): # self mean connection
        print(f"{self.name} is in class {self.grade} with {self.percentage} % ") 
  
#Object==instance of class....

student1=student("preeatm",11,96)
student2=student("rishab",12,95)

# print(student1.name)
print(student1.get_percentage())
print(student1.get_name()) #encapsulation
