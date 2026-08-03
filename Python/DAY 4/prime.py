num = int(input("Enter a number to check for prime number: "))
if num <= 1:
    print(f"{num} is Not Prime")
else:
    is_prime = True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if(is_prime==True):
        print(f"The number '{num}' is Prime")
    else:
        print(f"The number '{num}' is  Not Prime")