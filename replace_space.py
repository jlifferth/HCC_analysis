import os

# this script searches downstream file and folder names and replaces spaces with underscores

folder = input('target : ')


def replace_space(src_folder):
    print('formatting dir and file names...\n')
    rename_counter = 0
    for root, dirs, files in os.walk(src_folder):
        for directory in dirs:
            if ' ' in directory:
                new_directory = directory.replace(' ', '_')
                old_path = os.path.join(root, directory)
                new_path = os.path.join(root, new_directory)
                os.rename(old_path, new_path)
                print(old_path)
                print(new_path)
                rename_counter += 1
        for file in files:
            if ' ' in file:
                new_file = file.replace(' ', '_')
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
                print(old_path)
                print(new_path)
                rename_counter += 1
    print(str(rename_counter) + ' files and folders renamed\n')


replace_space(folder)
