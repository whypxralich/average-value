print ("Hello! Write me 5 numbers and I will find the arithmetic mean of these numbers!")
print ("Write something to continue!")
smth = input()

print ("Nice! Write the first number")
num1 = input()
if not num1.isdigit():
    print("Error: This is not a number.")
    exit()

print ("Write the second number")
num2 = input()
if not num2.isdigit():
    print("Error: This is not a number.")
    exit()

print ("Write the third number")
num3 = input()
if not num3.isdigit():
    print("Error: This is not a number.")
    exit()

print ("Write the fourth number")
num4 = input()
if not num4.isdigit():
    print("Error: This is not a number.")
    exit()

print ("Write the fifth number")
num5 = input()
if not num5.isdigit():
    print("Error: This is not a number.")
    exit()

numbers = [int(num1), int(num2), int(num3), int(num4), int(num5)]

total = sum(numbers)
count = len(numbers)
average = total / count
print (f"The arithmetic mean of these numbers is: {average}")