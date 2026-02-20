#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

""" 1
       """
#Abstration ==hiding unnecessary  details from users  through class and methods...
# class student:
#     def __init__(self,name,grade,percentage):# Method
#         self.name=name #attribute
#         self.grade=grade #attribute
#         self.percentage=percentage #attribute
#     def student_details(self):#method abstarction
#         print(f"{self.name} is in class {self.grade} with {self.percentage+2} % ") #+2 its hiddin by user     
  
# #Object==instance of class....

# student1=student("preeatm",11,96)
# student2=student("risha",12,95)
# student1.student_details()
# student2.student_details()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def Person_details (self):
#         print(f"student name{self.name} and is age is {self.age+1}")
    
# Person1=Person("reddy",23)
# print(Person1.age)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\    

""" 2
      """

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
        print(f"{self.name} IS IN CLASS {self.grade} WITH {self.percentage} % ") 
  
#Object==instance of class....

student1=student("KARAN",11,96)
student2=student("ARJUN",12,95)

# print(student1.name)
print(student1.get_percentage())
print(student1.get_name()) #encapsulation


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

""" 3
       """

# Inheritance :== allow on class (child to reuse the property nad methods of another 
# class(parent)

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
student2=student("risha",12,95)

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

# #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

""" 4  
       """

# class student:  # parent class
#     def __init__(self, name, grade, team):
#         self.name = name
#         self.grade = grade
#         self.team = team

#     def student_details(self):  # parent method
#         print(f"[Parent] Student: {self.name}, Grade: {self.grade}, Team: {self.team}")


# class Graduatestudent(student):  # child class
#     def __init__(self, name, grade, team, house):
#         super().__init__(name, grade, team)
#         self.house = house

#     def student_details(self):  # overriding (polymorphism)
#         print(f"[Child] Student: {self.name}, Grade: {self.grade}, "
#               f"Team: {self.team}, House: {self.house}")


# # objects
# stu1 = student("preetam", 23, "A")
# grad1 = Graduatestudent("reddy", 1, "C", "red")

# # polymorphism
# stu1.student_details()   # parent version
# grad1.student_details()  # child version

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class Bankaccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.__balance=balance

    def get__balance(self):
         return self.get__balance

    def deposit(self,amount):
        self.__balance+=amount

    def withdraw (self,amount):
          if self.__balance >=amount:
               self.__balance-=amount
          else:
              print("insuficient balance")
              
account=Bankaccount("1234567",1200)
print(account.get__balance())
account.deposit(100)
print(account.get__balance())
account.withdraw(1500)
print(account.get__balance())
