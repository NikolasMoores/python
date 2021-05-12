import shutil
import os

os.chdir('FilesToSort')

key_list = []
directory_types = {}
for directory_name, subdirectories, filenames in os.walk('.'):
    for file in filenames:
        filetype = file.split('.')
        if filetype[1] not in directory_types:
            what_sort = input(str('What category would you like to sort ' + filetype[1] + ' file into?'))
            if what_sort not in directory_types:
                directory_types[filetype[1]] = what_sort

            for key, value in directory_types.items():
                if value not in key_list:
                    key_list.append(value)
                    os.mkdir(value)

        shutil.move(directory_name + '/' + file, directory_types[filetype[1]] + '/' + file)
