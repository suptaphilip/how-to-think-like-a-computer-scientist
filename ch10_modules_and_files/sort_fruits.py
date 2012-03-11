input_file = open('unsorted_fruits.txt', 'r')
fruits = input_file.readlines()
input_file.close()
fruits.sort()
output_file = open('sorted_fruits.txt', 'w')
for fruit in fruits:
    output_file.write(fruit)
output_file.close()

