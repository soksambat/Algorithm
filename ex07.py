# Exercises: 07
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20
while True:
    num = int(input("Enter a number: "))
    if 10 <= num <= 20:
        print("Continue")
    else:
        print("Out of range")