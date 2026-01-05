class Rbi:
    def gold_loan(self):
        print("Gold loan rate:",8.5)
    def home_loan(self):
        print("Home loan rate:",9.2)
    def car_loan(self):
        print("Car loan rate:",8.5)

class Hdfc(Rbi):
    def gold_loan(self):
        print("Gold loan rate:",9.5)
    def home_loan(self):
        print("Home loan rate:",10)
    def car_loan(self):
        print("Car loan rate:",9.7)

loan_instance1=Hdfc()
loan_instance1.car_loan()

loan_instance2=Rbi()
loan_instance2.car_loan()
