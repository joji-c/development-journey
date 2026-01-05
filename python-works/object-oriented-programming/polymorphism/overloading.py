class Calculator:
    def add(self,num1,num2):
        print(num1+num2)#this will not work as python doesnt allow method overloading
    def add(self,num1,num2,num3):
        print(num1+num2+num3)#this is the only one that works

instance=Calculator()
instance.add(10,20,30)#the last add will work
instance.add(10,20)#this will not work it shows error 

"""
as we changed the value saved in add = num1+num2 to num1+num2+num3 the previous data is gone  
eg:- n=5
     n=10
     now n has a value of 10 , n=5 is gone
"""
