# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(self.name, "is eating")

# class Dog(Animal):
#     def bark(self):
#         print(self.name, "says Woof!")


# dog = Dog("Buddy")
# dog.eat()   
# dog.bark()  

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print(self.brand, "car is driving")


car = Car("Toyota")
car.start()  
car.drive()  