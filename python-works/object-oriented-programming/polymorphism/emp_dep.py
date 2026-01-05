class Employee:
    def __init__(self,id,department,salary):
        self.id=id
        self.department=department
        self.salary=salary
    def display(self):
        print(f"Id:{self.id}  Department:{self.department}  Salary:{self.salary}")

class Department(Employee):
    def __init__(self,id,department,salary,pro_lang,framework):
        super().__init__(id,department,salary)
        self.pro_lang=pro_lang
        self.framework=framework
    def display(self):
        super().display() 
        print(f"Programming language:{self.pro_lang}  Framework:{self.framework}")
    
dep_instance=Department(123,"hr",80000,"Python","nvt")
dep_instance.display()

"""here both employee and department class have display method which means it is a polymorphism, 
method overriding: which means two plpace same name different behavior"""
