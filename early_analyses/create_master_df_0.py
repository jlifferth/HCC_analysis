import os

# this script collects all track statistics csv files into a single csv for more efficient analysis

target_folder = '/Users/jonathanlifferth/Documents/Arbeit/Vanderbilt_Research_Analyst/' \
                'Naotoshi_Nakamura/2_trackmate_results/'

csv_name = 'master_df_1.csv'

# create and write master df header (use 'w' to overwrite csv)
out_file_header = 'IMAGE_SERIES,Label,TRACK_ID,NUMBER_SPOTS,NUMBER_GAPS,LONGEST_GAP,NUMBER_SPLITS,NUMBER_MERGES,' \
                  'NUMBER_COMPLEX,TRACK_DURATION,TRACK_START,TRACK_STOP,TRACK_DISPLACEMENT,TRACK_INDEX,' \
                  'TRACK_X_LOCATION,TRACK_Y_LOCATION,TRACK_Z_LOCATION,TRACK_MEAN_SPEED,TRACK_MAX_SPEED,' \
                  'TRACK_MIN_SPEED,TRACK_MEDIAN_SPEED,TRACK_STD_SPEED,TRACK_MEAN_QUALITY,TRACK_MAX_QUALITY,' \
                  'TRACK_MIN_QUALITY,TRACK_MEDIAN_QUALITY,TRACK_STD_QUALITY'
with open(csv_name, 'w') as out_file:
    out_file.write(out_file_header + '\n')
out_file.close()

count = 0
file_names = []
for root, dirs, files in os.walk(target_folder):
    for file in files:
        if file.endswith('Track statistics.csv'):
            print(file)
            file_names.append(os.path.join(root, file))
            current_file = os.path.join(root, file)
            img_series_name = file[:-21]
            with open(current_file, 'r') as in_file:
                next(in_file)
                for line in in_file:
                    with open(csv_name, 'a') as out_file:
                        out_file.write(img_series_name + ',' + line)
                        print(root)
                        print(line)
                        count += 1

print(file_names)
print("Number of files : " + str(len(file_names)))
print('total line count : ' + str(count))
