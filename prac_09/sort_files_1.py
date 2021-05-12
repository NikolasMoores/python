import shutil
import os


os.chdir('FilesToSort')

directory_types = []
for directory_name, subdirectories, filenames in os.walk('.'):
    for subdir in subdirectories:
        directory_types.append(subdir)
    for file in filenames:
        filetype = file.split('.')
        if filetype[1] not in directory_types:
            os.mkdir(filetype[1])
            directory_types.append(filetype[1])
        shutil.move(directory_name + '/' + file, filetype[1] + '/' + file)
