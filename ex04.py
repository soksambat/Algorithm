# Exercises: 04 We have text ="3 4 5 6"
# Q1: Display number 1 by one without space
number = input("Enter number:")
for char in number:
    if char !="":
        print(char)

# Q2: Sum all number (Total: 18)
number = input("Enter number: ")
sum = 0
for num in number:
    sum += int(num)
    print(sum)