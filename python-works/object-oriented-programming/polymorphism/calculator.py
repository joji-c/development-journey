class Calculator:
    def add(self,*num):
        print(sum(num))

cal=Calculator()

cal.add(1,3,5)
cal.add(2,4,6,8,10,15)
