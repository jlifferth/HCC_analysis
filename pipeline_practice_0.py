# subprocess_os_system.py
#  https://forum.image.sc/t/how-to-call-and-run-ilastik-from-python/22009/23

import os
from os import walk  # Find folders and files
from os import listdir
from os.path import isfile, join
import subprocess

# rename all files and folders, replace '\s' with '_' so that file paths are compatible with headless
# function when subprocess is called
folder = '/Users/jonathanlifferth/Documents/Arbeit/Vanderbilt_Research_Analyst/' \
         'Naotoshi_Nakamura/_original_images/_Inhibitors/JHH6_0uM/JHH6_0uM_n1/'


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

# Test from forum @CellKai
ilastik_location = '/Applications/ilastik-1.4.0b15-OSX.app/Contents/ilastik-release'
ilastik_project = '/Users/jonathanlifferth/HCC_pipeline_0.ilp'

indir = '/Users/jonathanlifferth/Documents/Arbeit/Vanderbilt_Research_Analyst/' \
         'Naotoshi_Nakamura/_original_images/_Inhibitors/JHH6_0uM/JHH6_0uM_n1/'
infile = 'A1_03_1_1_Bright_Field_002.tif'

command = '/Applications/ilastik-1.4.0b15-OSX.app/Contents/ilastik-release/run_ilastik.sh' \
          ' --headless --project=/Users/jonathanlifferth/HCC_pipeline_0.ilp ' \
          '--export_source="simple segmentation" --raw_data=' + indir + infile

# subprocess.call(command, shell=True)

# perform segmentation on all original images
tif_count = 0
for root, dirs, files in os.walk(folder):
    for file in files:
        if file[-4:] == '.tif':
            print(file)
            path = os.path.join(root, file)
            command = '/Applications/ilastik-1.4.0b15-OSX.app/Contents/ilastik-release/run_ilastik.sh' \
                      ' --headless --project=/Users/jonathanlifferth/HCC_pipeline_0.ilp ' \
                      '--export_source="simple segmentation" --raw_data=' + path
            subprocess.call(command, shell=True)
            print(file + ' segmented')
            tif_count += 1
print('tifs segmented : ' + str(tif_count))
print('segmentation complete')
