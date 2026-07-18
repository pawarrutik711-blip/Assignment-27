# write a python program to implement the class named numbers with the falling specification


class Numbers:

    def __init__(self):
        self.value = int(input("Enter number:"))

    def chkprime(self):
        if self.value <= 1:
            print("not prime number")
            return
        for i in range(2, self.value):
            if self.value % i == 0:
                print("not prime")
                return
        print("prime")

    def chkperfect(self):
        s = 0
        for i in range(1, self.value):
            if self.value % i == 0:
                s += i
        if s == self.value:
            print("perfect number")
        else:
            print("not perfect number")

    def factors(self):
        print("factors are:")
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                print(i, end=" ")
        print()

    def sumfactors(self):
        s = 0
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                s += i
        print("sum of factors is:", s)

obj1 = Numbers()
obj1.chkprime()
obj1.chkperfect()
obj1.factors()
obj1.sumfactors()

