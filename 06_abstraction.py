from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class MyATM(ATM):
    def withdraw(self, amount):
        print(amount, "rupees nikaale")


atm = MyATM()
atm.withdraw(1000)