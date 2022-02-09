# preliminary analysis using master_df_0.csv
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

master_df = pd.read_csv('../master_df_0.csv')
columns = ['IMAGE_SERIES', 'Label', 'TRACK_ID', 'NUMBER_SPOTS', 'NUMBER_GAPS',
           'LONGEST_GAP', 'NUMBER_SPLITS', 'NUMBER_MERGES', 'NUMBER_COMPLEX',
           'TRACK_DURATION', 'TRACK_START', 'TRACK_STOP', 'TRACK_DISPLACEMENT',
           'TRACK_INDEX', 'TRACK_X_LOCATION', 'TRACK_Y_LOCATION',
           'TRACK_Z_LOCATION', 'TRACK_MEAN_SPEED', 'TRACK_MAX_SPEED',
           'TRACK_MIN_SPEED', 'TRACK_MEDIAN_SPEED', 'TRACK_STD_SPEED',
           'TRACK_MEAN_QUALITY', 'TRACK_MAX_QUALITY', 'TRACK_MIN_QUALITY',
           'TRACK_MEDIAN_QUALITY', 'TRACK_STD_QUALITY']
print(master_df.columns)
sns.boxplot(x='IMAGE_SERIES', y='TRACK_MEAN_SPEED', data=master_df)
plt.xticks(rotation=65)
axes = plt.gca()
plt.title('Track mean speed by cell line')
plt.ylabel('pixels per track link')
plt.xlabel('cell line')
plt.show()
