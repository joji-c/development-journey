class Bank:
    acc_num=int
    name=str
    acc_type=str
    balance=int

    def set_acc(self,acc_num,name,acc_type,balance):
        self.acc_num=acc_num
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"you have credited {amount} to your account {self.acc_num} ,your balance is {self.balance}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"you have withdrawn {amount} from your account {self.acc_num} ,your balance is {self.balance}")
        else:
            print("transaction failed due to insufficient balance")

    def show_balance(self):
        print(f"{self.name}'s current balance is {self.balance}")

bank_instance1=Bank()
bank_instance1.set_acc(123,"joji","deposit",1000)

bank_instance1.show_balance()
bank_instance1.deposit(4000)
bank_instance1.withdraw(500)
