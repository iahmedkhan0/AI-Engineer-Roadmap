#simple interest
principalamnt = float(input("Enter the principal amount = "))
roi = float(input("Enter the Rate of interest per year (in %) = "))
time = float(input("Enter the time in years = "))

interest = (principalamnt*time*roi)/100

print("The simple interest is = ",interest)
total_amount = principalamnt+interest
print("The total amount = ",total_amount)