
min_length = 2


print("Enter Password")

valid = False

while valid == False:
    password = input("> ")
    if len(password) < min_length:
        print("Invalid Length")
    else:
        asterisk = '*'
        for i in range(0, len(password)-1, 1):
            asterisk = asterisk+'*'
        print(asterisk)
        valid = True


