# exercise 3
# 1
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
# 2
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    print("Error: Please enter an integer.")
# 3
try:
    numbers = [10, 20, 30, 40, 50]

    index = int(input("Enter the index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Error: Index is out of range.")

except ValueError:
    print("Error: Please enter an integer.")
