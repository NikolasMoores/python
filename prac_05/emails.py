email_list = {}
email = input("Enter email: ")
while email != "":
    email_name = email.split('@')
    name_correct = input('Is your name {}? (Y/n)'.format(email_name[0]))
    name_correct = name_correct.upper()
    if name_correct == 'Y' or name_correct == '':
        email_list[email] = email_name[0]
    elif name_correct == 'N':
        name = input("Enter name: ")
        email_list[email] = name
    email = input("Enter email: ")

for key, value in email_list.items():
    print('{} ({})'.format(value,key))
