#Exercise2
numbers = []

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

evens = list(filter(lambda x: x % 2 == 0, numbers))

result = list(map(lambda x: x + 15, evens))

print("Your Data:", result)
