import os

# practice manipulating string to pull img_series_name out of file path name

path = '/Users/jonathanlifferth/Documents/Arbeit/Vanderbilt_Research_Analyst/Naotoshi_Nakamura/' \
       '2_trackmate_results/_Inhibitors/JHH6_0uM/JHH6_0uM_n1/'

path = path.split('/')
path = path[-2]
print(path)

target_folder = '/Users/jonathanlifferth/Documents/Arbeit/Vanderbilt_Research_Analyst/' \
                'Naotoshi_Nakamura/2_trackmate_results/'

for root, dirs, files in os.walk(target_folder):
    for file in files:
        if file.endswith('Track statistics.csv'):
            print(file)
            current_file = os.path.join(root, file)
            print(root)
            img_series_name = root.split('/')
            img_series_name = img_series_name[-1]
            print(img_series_name)
