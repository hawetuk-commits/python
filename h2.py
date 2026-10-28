# Exercise_1
#1
def person_info(username, age):
    print(f"Hello {username}!")
    print(f"You are {age} years old.")

    birth_year = 2026 - age
    print(f"You were born in {birth_year}")


name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))

person_info(name, age)


#2
def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))


print(f"The sum of {num1} and {num2} is: {add(num1, num2)}")
print(f"The difference of {num1} and {num2} is: {sub(num1, num2)}")
print(f"The product of {num1} and {num2} is: {multi(num1, num2)}")
print(f"The quotient of {num1} and {num2} is: {div(num1, num2)}")
