class Factorial:
    def facto(self,number):
        fact=1
        for i in range(1,number+1):
            fact*=i
        print(fact)
fact_instance=Factorial()
fact_instance.facto(5)
