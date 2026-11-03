try:
    age = int(input("How old are you?"))
    print("Next year, you’ll be", age + 1)
except ValueError:
    print("Please enter your age as a number.")