import os

# this script removes ALL downstream files (but not directories) from specified path

print('this script removes ALL downstream files\n(but not directories) from specified path')
path_input = input('specify path: ')


def remove_downstream(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(file + '\nremoved successfully')

    # check if files were successfully removed
    for root, dirs, files in os.walk(path):
        for file in files:
            print(root, file)


remove_downstream(path_input)

# /Users/jonathanlifferth/Documents/Arbeit/Vanderbilt_Research_Analyst/Naotoshi_Nakamura/
# image template folders (blank)/_Inhibitors
