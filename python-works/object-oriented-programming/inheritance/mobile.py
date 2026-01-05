class Mobile:
    def __init__(self,brand,model,price,features):
        self.model=model
        self.price=price
        self.brand=brand
        self.features=features
    def display(self):
        print(f"The {self.brand} {self.model} is priced at {self.price} and comes with a {self.features}")

mobile_instance1=Mobile("Samsung","S24","84,000","stylous pen")
mobile_instance1.display()

mobile_instance2=Mobile("One plus","13","72,000","telephoto camera")
mobile_instance2.display()

mobile_instance3=Mobile("Apple","Air","132,000","super slim design")
mobile_instance3.display()
