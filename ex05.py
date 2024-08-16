# # Exercises: 05
text ="454639"
# # # Q1: Count odd and even number in texe
odd_count = 0
even_count = 0
for char in text:
    num = int(char)
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(even_count, odd_count)

# # Q2: sum all number 
text ="454639"
sum = 0
for num in text:
    sum += int(num)
    print(sum)

# # Q3: sum only even number
text ="454639"
sum = 0
for char in text:
    if int(char) % 2 == 0:
        sum += int(char)
print(sum)

# Q4: Print Reverse number
text ="454639"
result = ""
lastIndex = len(text) - 1
for i in range(lastIndex, -1, -1):
    result += text[i]
    print(result)
