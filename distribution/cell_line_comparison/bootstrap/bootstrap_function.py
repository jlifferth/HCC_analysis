import numpy as np


def perform_bootstrap(dataframe, cell_line):
    df = dataframe
    cell_line_df = df[df['cell_line'] == cell_line]
    TRACK_MEAN_SPEED_df = cell_line_df[['TRACK_MEAN_SPEED', 'IMAGE_SERIES']]
    cell_line_list = TRACK_MEAN_SPEED_df.IMAGE_SERIES.unique()

    # perform loop to identify max length for all image series for this cell line
    max_length = 0
    for series in cell_line_list:
        series = TRACK_MEAN_SPEED_df[TRACK_MEAN_SPEED_df['IMAGE_SERIES'] == series]
        series_length = len(series)
        if series_length > max_length:
            max_length = series_length
        else:
            pass

    print('max_length: ', max_length)
    bootstrap_dict = {}

    # next, use the max length to bootstrap values for any series with fewer values than the max length
    for series in cell_line_list:
        series_values = TRACK_MEAN_SPEED_df[TRACK_MEAN_SPEED_df['IMAGE_SERIES'] == series]['TRACK_MEAN_SPEED']
        series_length = len(series_values)
        if series_length < max_length:
            x = np.random.choice(series_values, size=max_length, replace=True)
            bootstrap_dict[series] = x
        elif series_length == max_length:
            bootstrap_dict[series] = series_values
        else:
            print('Series length error')

    print(bootstrap_dict.keys())
    return bootstrap_dict
