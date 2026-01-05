class Car:
    name:str
    brand:str
    price:int
    color:str

    def set_car(self,name,brand,price,color):
        self.name=name
        self.brand=brand
        self.price=price
        self.color=color
    
    def display(self):
        print("car name: ",self.name)
        print("car brand: ",self.brand)
        print("car price: ",self.price)
        print("car color: ",self.color)

car_instance1=Car()
car_instance1.set_car("S class","Benz",5000000,"black")
car_instance1.display()
