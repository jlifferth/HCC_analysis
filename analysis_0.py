import pandas as pd
import numpy as np


# this script retrieves track statistics for specific cell lines generates from trackmate results


def get_src(target_cell_line, target_sub_series):
    src_folder = '/Users/jonathanlifferth/Documents/Arbeit/Vanderbilt Research Analyst/' \
                'Naotoshi Nakamura/_trackmate results 1/'
    cell_line = target_cell_line
    sub_series = target_sub_series
    src = src_folder + cell_line + '/' + sub_series + '/' + sub_series + ' Track statistics.csv'
    return src


# call JHH4 cell line
JHH4_A2 = get_src(target_cell_line='JHH4', target_sub_series='JHH4 A2')
JHH4_B2 = get_src(target_cell_line='JHH4', target_sub_series='JHH4 B2')
JHH4_C2_Pickup = get_src(target_cell_line='JHH4', target_sub_series='JHH4 C2 Pickup')
JHH4_D2 = get_src(target_cell_line='JHH4', target_sub_series='JHH4 D2')

# assign dataframes
JHH4_A2_df = pd.read_csv(JHH4_A2)
JHH4_B2_df = pd.read_csv(JHH4_B2)
print(JHH4_B2_df)
JHH4_C2_Pickup_df = pd.read_csv(JHH4_C2_Pickup)
JHH4_D2_df = pd.read_csv(JHH4_D2)


# calculate mean velocities
JHH4_A2_mean_of_mean_velocities = np.mean(JHH4_A2_df.TRACK_MEAN_SPEED)
JHH4_B2_mean_of_mean_velocities = np.mean(JHH4_B2_df.TRACK_MEAN_SPEED)
JHH4_C2_Pickup_mean_of_mean_velocities = np.mean(JHH4_C2_Pickup_df.TRACK_MEAN_SPEED)
JHH4_D2_mean_of_mean_velocities = np.mean(JHH4_D2_df.TRACK_MEAN_SPEED)

# print mean velocities
print('\ntotal mean velocities \n')
print('JHH4_A2 : ' + str(JHH4_A2_mean_of_mean_velocities))
print('JHH4_B2 : ' + str(JHH4_B2_mean_of_mean_velocities))
print('JHH4_C2 Pickup : ' + str(JHH4_C2_Pickup_mean_of_mean_velocities))
print('JHH4_D2 : ' + str(JHH4_D2_mean_of_mean_velocities))
