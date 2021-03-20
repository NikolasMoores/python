# question 1
name_file = open("name.txt", 'w')

name = str(input("Enter the name: "))
print("{}".format(name), file=name_file)

name_file.close()

# question 2
name_read = open("name.txt", "r")
print("Your name is {}".format(name_read.read()))

# question 3
num_file = open("numbers.txt", 'w')

numbers = [17, 42, 400]
for i in numbers:
    print("{:<3}".format(i), file=num_file)

num_file.close()

num_read = open("numbers.txt", "r")
first = num_read.readline()
second = num_read.readline()
first_two = int(first) + int(second)
print(first_two)

num_read.close()

# question 4
num_read = open("numbers.txt", "r")

total = 0
for lines in num_read:
    total = total + int(lines)
print(total)

num_read.close()