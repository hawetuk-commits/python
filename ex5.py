# Question1
number = 7

for attempt in range(5):
    guess = int(input("Guess the number: "))

    if guess == number:
        print("Correct!")
        break

    print("Wrong!")

else:
    print("You are out of attempts!")

# Question2

number = int(input("Enter a number: "))

sum = 0

while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10

print("Sum is:", sum)
