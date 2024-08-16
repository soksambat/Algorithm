
# Exercises: 03 Enter text and check if it contains capital letter or not
text = input("Enter text: ")
isCapital = False
isCapital = True
for i in range(len(text)):
    if text[i].isupper():
        isCapital = True 
        print("Yes")
    else:
        text[i].isupper()
        isCapital = False 
        print("No")