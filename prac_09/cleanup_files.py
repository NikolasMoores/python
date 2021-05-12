"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name_enumerated = list(enumerate(new_name))
    new_name = ''
    was_capital = True
    is_letter = True
    for letter in new_name_enumerated:
        if was_capital is False:
            if letter[1] != '_' and letter[1].isupper():
                new_name = new_name+'_'
        if letter[1].isupper() or letter[1] == '_':
            was_capital = True
        else:
            was_capital = False
        if is_letter is False and letter[1].isalpha():
            new_name = new_name + letter[1].upper()
        else:
            new_name = new_name + letter[1]
        if letter[1].isalpha():
            is_letter = True
        elif letter[1] == '.':
            is_letter = True
        else:
            is_letter = False
    return new_name


# main()


test_name = ['Away In A Manger.txt', 'SilentNight.txt', 'O little town of bethlehem.TXT', 'ItIsWell (oh my soul).txt']
for name in test_name:
    name_get = get_fixed_filename(name)
    print(name_get)
