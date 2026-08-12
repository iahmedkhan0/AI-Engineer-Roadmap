numbers = [12, 45, 7, 89, 34, 56]
largest = numbers[0]
second_largest = numbers[1]

for i in numbers:
    if i>largest:
        second_largest = largest
        largest = i
    elif i>second_largest:
        second_largest = i
print(second_largest)