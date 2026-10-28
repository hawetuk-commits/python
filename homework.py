# Question 1:
gtst = "Day 7"


# Question 2:
print(f"Hello Today is our {gtst} course")


# Question 3:
numbers = [0, 2, 4]

print(f"The 1st Even number is {numbers[0]}")
print(f"The 2nd Even number is {numbers[1]}")
print(f"The 3rd Even number is {numbers[2]}")


# Question 4:
fruits = {
    "apple": 10,
    "banana": 15,
    "pineapple": 20
}


# Question 5:

# a) Pseudocode:
#
# START
#
# Create diction
# ary fruits
#     apple = 10
#     banana = 15
#     pineapple = 20
#
# Ask the user to enter a fruit
# Store the answer in choice
#
# Find the value of choice in fruits
#
# Display:
# "The value of choice is value birr"
#
# END


# b) Python code:
choice = input("Enter your fruit: ")

print(f"The value of {choice} is: {fruits[choice]} birr")
