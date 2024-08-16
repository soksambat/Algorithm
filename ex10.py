# Exercises: 10
# Enter 5 number and find maxiamuu and minimum ValueError
find = ''
for i in range(5):
    number = input("Enter number: ")
    find += str(number)
    max = 0
    min = 0
for j in range(len(find)):
    if int(find[j]) > max:
        max = int(find[j])
    if int(find[j]) < min:
        min = int(find[j])
print(max,min)
