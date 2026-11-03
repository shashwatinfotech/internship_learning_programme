# class Car:
#     def __init__(self, brand, model, color, year):
#         self.brand = brand
#         self.model = model
#         self.color = color
#         self.year = year

#     def show_details(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Color:", self.color)
#         print("Year:", self.year)


# car1 = Car("Toyota", "Corolla", "White", 2022)
# car1.show_details()

class car:
    def __init__(self, brand, model, color,price):
        self.brand = brand
        self.model = model
        self.color = color 
        self.price = price 
        
    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Year:", self.price)
    
car1 = car("toyota", "xl", "red" , 2100 )
car1.show_details()        
