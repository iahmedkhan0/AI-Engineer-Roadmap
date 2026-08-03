num = int(input("Enter a number for which factorial is needed: "))
result = 1
for num in range(num,0,-1):
    result = result * num
print(result)