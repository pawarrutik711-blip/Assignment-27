# write a python program to implement a class named bankaccount with the follwing requirement



class Bankaccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def display(self):
        print("Account holder name is:", self.name, "And account balance is:", self.amount)

    def deposit(self):
        ret = int(input("Enter the amount you wanted to deposit:"))
        self.amount += ret
        print("Now your Account Balance is:", self.amount)

    def withdraw(self):
        ret = int(input("Enter the amount you want to withdraw:"))
        if self.amount >= ret:
            self.amount -= ret
            print("Now your Account Balance is:", self.amount)
        else:
            print("Account Balance is low")
    def calculateinterest(self):
        intrest = self.amount * self.ROI / 100
        print("Your intrest is:", intrest)
obj1 = Bankaccount("Rutik Rahul Pawar", 1000)
obj1.display()
obj1.deposit()
obj1.withdraw()
obj1.calculateinterest()

