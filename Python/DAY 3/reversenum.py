num = int(input("Enter a number: "))
og = num
reverse = 0
while num!=0:
    last_dig = num%10
    reverse = (reverse*10)+last_dig
    num //= 10 
print(reverse)