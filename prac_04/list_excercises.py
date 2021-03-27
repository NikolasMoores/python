numbers = []
for i in range(0,5,1):
    number = int(input("Number: "))
    numbers.append(number)

average = sum(numbers)/len(numbers)
print("The first number is {}\n"
      "The last number is {}\n"
      "The smallest number is {}\n"
      "The largest number is {}\n"
      "The average of the numbers is {}".format(numbers[0],numbers[4],min(numbers),max(numbers),average))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("access granted")
else:
    print("access denied")