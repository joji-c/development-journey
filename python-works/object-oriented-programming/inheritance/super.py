class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f"Name: {self.name} Age: {self.age} Gender: {self.gender}")

class Student(Person):
    def __init__(self,name,age,gender,rol,course):
        super().__init__(name,age,gender)
        self.rol=rol
        self.course=course
    def display(self):
        super().display()
        print(f"Rollnum: {self.rol} Course: {self.course} ")


student_instance=Student("joji",22,"male",62,"data science")
student_instance.display()
