# Read a number from the user
number = int(input("Enter a number: "))

# Display corresponding day using if-elif-else
if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("Invalid number. Please enter a number between 1 and 7.")