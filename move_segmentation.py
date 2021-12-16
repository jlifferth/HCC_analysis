import os
import shutil

# this script moves all segmented tif images from the '_original_images' folder
# and places them in the appropriate 'i_segmented_images' folder for reference

# for example: /original_images/cell_line_1/segmented_image.tif
# will be moved to /1_segmented_images/cell_line_1/segmented_image.tif

print('\nthis script moves segmented tif images from the "_original_images" folder \n'
      'and places them in the appropriate "i_segmented_images" folder for future reference')
cell_line_path = input('\ncell line to move (absolute path) : ')
cell_line_dst = input('\ndestination (just enter "i_segmented_images" where i represents experiment number) : ')
print('\nmoving ', cell_line_path, ' ... to \n', cell_line_dst)


def move_segmentation(cell_line, dst):
    count_1 = 0
    count = 0
    for root, dirs, files in os.walk(cell_line):
        for file in files:
            count_1 += 1
            if file[-16:] == "Segmentation.tif":
                file_path = os.path.join(root, file)
                # print(file_path)
                file_path_list = file_path.split('/')
                print(file_path_list[7])
                file_path_list[7] = dst
                new_file_path = '/'.join(file_path_list)
                print(new_file_path)
                shutil.move(file_path, new_file_path)
                count += 1
    print(count, ' files of any type found')
    print(count, 'segmentation files found and moved')


move_segmentation(cell_line_path, cell_line_dst)
