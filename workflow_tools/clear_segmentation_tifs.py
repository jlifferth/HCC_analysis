import os

folder = '/Users/jonathanlifferth/Documents/Arbeit/Vanderbilt_Research_Analyst/' \
         'Naotoshi_Nakamura/2_trackmate_results/_Inhibitors'


def clear_segmentation_tifs(src_folder):
    counter = 0
    counter_2 = 0
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file[-4:] == ".tif":
                # if file[-16:] == "Segmentation.tif":
                print(file + ' is segmentation')
                counter += 1
                path = os.path.join(root, file)
                os.remove(path)
                print(file + ' removed')
            elif file[-4:] == '.tif' and file[-16:] != "Segmentation.tif":
                counter_2 += 1

    print(str(counter) + ' segmentations found')
    print(str(counter_2) + ' non-segmentations found')


# clear_segmentation_tifs(folder)
