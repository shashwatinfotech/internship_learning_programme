# Example 1: File mein likhna; purana content replace hoga
with open("notes.txt", "w") as file:
    file.write("Hello Python")

# Example 2: File se poora text padhna
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Example 3: File ke end mein text jodna
with open("notes.txt", "a") as file:
    file.write("\nNayi line")

# Example 4: File ko line by line padhna
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())

# Example 5: File mein kai lines likhna
lines = ["Apple\n", "Mango\n", "Banana\n"]
with open("fruits.txt", "w") as file:
    file.writelines(lines)
    print(lines)