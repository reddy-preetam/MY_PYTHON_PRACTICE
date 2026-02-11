class student:  # parent class
    def __init__(self, name, grade, team):
        self.name = name
        self.grade = grade
        self.team = team

    def student_details(self):  # parent method
        print(f"[Parent] Student: {self.name}, Grade: {self.grade}, Team: {self.team}")


class Graduatestudent(student):  # child class
    def __init__(self, name, grade, team, house):
        super().__init__(name, grade, team)
        self.house = house

    def student_details(self):  # overriding (polymorphism)
        print(f"[Child] Student: {self.name}, Grade: {self.grade}, "
              f"Team: {self.team}, House: {self.house}")


# objects
stu1 = student("preetam", 23, "A")
grad1 = Graduatestudent("bhai", 1, "C", "red")

# polymorphism
stu1.student_details()   # parent version
grad1.student_details()  # child version
