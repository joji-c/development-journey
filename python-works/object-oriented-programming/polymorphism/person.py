class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    @property
    def get_age(self):
        print(self.age)
        
    def get_gender(self):
        print(self.gender)

person_instance1=Person("joji",22,"male")
person_instance1.get_age#here we have @property so no need for () as it is a property and not a method
person_instance1.get_gender()#here we are calling a method
print(person_instance1.name)#here we are calling the name from the object externally 
