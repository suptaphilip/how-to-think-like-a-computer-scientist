from sys import argv

numbers = argv[1:]
sum = 0

for number in numbers:
    sum += float(number)
mean = sum / len(numbers)

print mean
