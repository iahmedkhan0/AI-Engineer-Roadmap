num = int(input("Enter a number: "))
a = 0
b = 1
print(a,end=" ")
print(b,end=" ")
for i in range(num-2):
    c = a+b
    print(c,end=" ")
    a=b
    b=c