# subprocess_os_system.py

import os
import time
import subprocess
import sys

# time script
start = time.time()

folder = sys.argv[1]
# dst_folder = sys.argv[2]

# rename all files and folders, replace '\s' with '_' so that file paths are compatible with headless
# function when subprocess is called


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

tif_count = 0
path_string = ''
print(path_string)
# perform segmentation on all original images
for root, dirs, files in os.walk(folder):
    for file in files:
        # make sure that we don't re-segment any segmented images
        if file[-4:] == '.tif' and file[-16:] != "Segmentation.tif":
            print(file)
            path = os.path.join(root, file)
            path_string += ' ' + path
            tif_count += 1

print('path string: ' + path_string)

command = '/Applications/ilastik-1.4.0b15-OSX.app/Contents/ilastik-release/run_ilastik.sh' \
                      ' --headless --project=/Users/jonathanlifferth/HCC_pipeline_1.ilp ' \
                      '--export_source="simple segmentation" ' + path_string

subprocess.call(command, shell=True)
print('\ntifs segmented : ' + str(tif_count))
print('segmentation complete')

end = time.time()
print('time elapsed : ' + str(end - start) + ' seconds\n')
