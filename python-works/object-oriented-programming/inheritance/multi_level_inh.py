class Grandparent:
    def property(self):
        print("50 acre land and house")

class Parent(Grandparent):
    def vehicle(self):
        print("Maruti swift")
    
class Child(Parent):
    def gadgets(self):
        print("Nothing 2 smart phone")
    
child_instance=Child()
child_instance.property()
child_instance.vehicle()
child_instance.gadgets()
