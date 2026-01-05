#example for overriding
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(self.name,"sound")

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print(self.name,"bark")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        print(self.name,"meow")

dog_instance=Dog("tobby")
dog_instance.sound()

cat_instance=Cat("kitty")
cat_instance.sound()
