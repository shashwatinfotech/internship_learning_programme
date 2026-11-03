# class BankAccount:
#     def __init__(self, balance):
#         self._balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount

#     def show_balance(self):
#         print("Balance:", self._balance)


# account = BankAccount(1000)
# account.deposit(500)
# account.show_balance()

# class Wallet:
#     def __init__(self, money):
#         self._money = money

#     def add_money(self, amount):
#         if amount > 0:
#             self._money += amount

#     def show_money(self):
#         print("Wallet mein:", self._money, "rupees")


# my_wallet = Wallet(200)
# my_wallet.add_money(100)
# my_wallet.show_money()

class Pakit:
    def __init__(self, kharcho):
        self.kharcho = kharcho 
        
    def add_kharcho(self , amount):
        if amount > 0:
            self.kharcho += amount
        
    def show_money(self):
        print("pakit ma:", self.kharcho)
        
k = Pakit(200)
k.add_kharcho(100)
k.show_money()        
        
