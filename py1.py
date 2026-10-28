# Exercise 1
number = input("Enter a number: ")

if number.isdigit():
    number = int(number)

    if number % 2 == 0:
        print("This number is Even")
    else:
        print("This number is Odd")
else:
    print("Please enter a number only.")


# Exercise 2
number = int(input("Enter an integer: "))

if number > 0:
    print("The number is Positive")
elif number < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


# Exercise 3
score = int(input("Enter student's score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Exercise 4
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3

print("The largest number is:", largest)
