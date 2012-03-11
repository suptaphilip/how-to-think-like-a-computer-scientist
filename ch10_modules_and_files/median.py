from sys import argv

numbers = argv[1:]
for index in range(len(numbers)):
    numbers[index] = int(numbers[index])
numbers.sort()
length = len(numbers)

if length % 2 != 0:
    print numbers[length / 2]
else:
    print (numbers[length / 2 - 1] + numbers[length / 2]) / 2.0

