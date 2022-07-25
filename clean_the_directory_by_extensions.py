import os
import shutil
from os import listdir
from os.path import isfile, join

current_path = os.getcwd()
path_to_clean = r'C:\Users\Bartosz\Downloads'
file_in_path_to_clean = os.listdir(path_to_clean)
print(f'current directory is: {path_to_clean}')
onlyfiles = [f for f in listdir(path_to_clean) if isfile(join(path_to_clean, f))]
print(f'List of files in {path_to_clean} is {onlyfiles}')

extensions_file_list = []
for file in onlyfiles:
    try:
        extension = file.split('.')[1]
        extensions_file_list.append(extension)
    except IndexError:
        pass

extensions_file_list = set(extensions_file_list)
print(extensions_file_list)

for extensions in extensions_file_list:
    for file in onlyfiles:
        try:
            file_extension = file.split('.')[1]
            if extensions == file_extension and file_extension != 'py' and not os.path.exists(
                    path_to_clean + "\\" + extensions):
                new_path = path_to_clean + "\\" + extensions
                path_to_file = path_to_clean + "\\" + file
                print(path_to_file)
                os.mkdir(new_path)
                shutil.move(path_to_file, new_path)
            elif extensions == file_extension and file_extension != 'py':
                new_path = path_to_clean + "\\" + extensions
                path_to_file = path_to_clean + "\\" + file
                print(path_to_file)
                shutil.move(path_to_file, new_path)
        except IndexError:
            continue
