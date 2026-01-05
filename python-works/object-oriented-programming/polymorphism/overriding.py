class Parent:
    def properties(self):
        print("50lkh 10kg gold 10acr land")
    def bride(self):
        print("shradha")

class Child(Parent):
    def bride(self):
        print("shrishti")
    
#child_instance=Child()
#child_instance.bride()#here we modify the parent method to show the childs wifes name and not his fathers wife name as his


class Vehicle:
    def __init__(self,brand,title):
        self.brand=brand
        self.title=title
    def move(self):
        print(self.title,"is moving")

class Car(Vehicle):
    def __init__(self,brand,title):
        super().__init__(brand,title)

class Ship(Vehicle):
    def __init__(self,brand,title):
        super().__init__(brand,title)
    def move(self):
        print(self.title,"is sailing")

car_instance=Car("toyota","fortuner")
car_instance.move()

ship_instance=Ship("white star line","titanic")
ship_instance.move()
