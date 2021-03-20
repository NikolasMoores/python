def main():

    min_length = 2


    print("Enter Password")

    password = get_password(min_length)
    asterisk = print_asterisk(password)
    print(asterisk)

def print_asterisk(password):
    asterisk = '*'
    for i in range(0, len(password) - 1, 1):
        asterisk = asterisk + '*'
    return asterisk


def get_password(min_length):
    valid = False
    while valid == False:
        password = input("> ")
        if len(password) < min_length:
            print("Invalid Length")
        else:
            valid = True
    return password


main()