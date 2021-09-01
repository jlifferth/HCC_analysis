import os

# having trouble in inhibitor_analysis_0.ipynb locating files in the JHH6 2.5uM folder
# this script is to practice locating those files

# with open('/Users/jonathanlifferth/Documents/Arbeit/Vanderbilt Research Analyst/'
#           'Naotoshi Nakamura/1_trackmate_results/_Inhibitors/JHH6 2.5uM/JHH6 2.5uM n1/'
#           'JHH6 2.5 uM n1 Track statistics.csv', 'r') as in_file:
#     for file in in_file:
#         print(file)

src_folder = '/Users/jonathanlifferth/Documents/Arbeit/Vanderbilt Research Analyst/' \
             'Naotoshi Nakamura/1_trackmate_results/_Inhibitors/JHH6 2.5uM/JHH6 2.5uM n1/'

for infile in os.listdir(src_folder):
    print(infile)
