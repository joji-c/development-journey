class Father:
    def father_skills(self):
        print("cricket skills")
    
class Mother:
    def mother_skills(self):
        print("cooking skills")
    
class Child(Father,Mother):
    pass

child_instance=Child()
child_instance.father_skills()
child_instance.mother_skills()
