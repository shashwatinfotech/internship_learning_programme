student = {"name": "Asha", "age": 21, "city": "Pune"}

print(student["name"])           # Asha
print(student.get("age"))        # 21
student["age"] = 22               # value update
del student["city"]               # key-value remove
print(student["age"])