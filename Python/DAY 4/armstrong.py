num = int(input("Enter a number: "))
og=num
total = 0
while num!=0:
    dig = num%10
    total = total+(dig**3)
    num//=10
print("Total is : ", total)
if (total==og):
    print("Armstrong number")
else:
    print("Not Armstrong Number")