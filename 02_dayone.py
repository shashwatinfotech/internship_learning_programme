class Student:
    def __init__(self, name, age, grade, student_id):
        self.name = name 
        self.age = age 
        self.grade = grade 
        self.student_id = student_id
        
    def display(self):
        print("name:", self.name)
        print("age:", self.age)
        print("grade:", self.grade)
        print("student_id:", self.student_id)
        
student1 = Student("chaitanya", 18, "S101", 12)
student2 = Student("deep", 16, "S102", 11)
student3 = Student("manav", 15, "S103", 12)
student4 = Student("het", 14, "S104", 11)

student1.display()
student2.display()
student3.display()
student4.display()

# class Car:
#     def __init__(self, car_name, model , price):
#         self.car_name = car_name
#         self.model = model 
#         self.price = price 
        
#     def display(self):
#         print("car_name:", self.car_name)
#         print("car_model:", self.model)
#         print("car_price:", self.price)
        
# c1 = Car("suzuki", "ab", 2100)
# c2 = Car("nexa", "ba", 3100)

# c1.display()
# c2.display()





        
               
    