import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None


def set_tiddies(raw_df, bad_rows: int, ):
    y_values = ['DDD', 'CCC', 'BBB', 'AAA', 'ZZ', 'YY', 'XX', 'WW', 'VV', 'UU', 'TT', 'SS', 'RR', 'QQ', 'PP', 'OO',
                'NN', 'MM', 'LL', 'KK', 'JJ', 'II', 'HH', 'GG', 'FF', 'EE', 'DD', 'CC', 'BB', 'AA', 'Z', 'Y', 'X',
                'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D',
                'C', 'B', 'A']

    trim_df_1 = raw_df[raw_df['Y-axis'] != 0]
    trim_df_2 = trim_df_1
    for i in range(bad_rows):
        trim_df_2 = trim_df_2[trim_df_2['Y-axis'] != trim_df_2['Y-axis'].max()]
    trim_df_3 = trim_df_2[trim_df_2['X-axis'] != trim_df_2['X-axis'].max()]

    y_coords = trim_df_3['Y-axis'].unique()

    flip_df = trim_df_3.iloc[::-1]
    flip_df["Y-value"] = np.nan

    for i in range(len(y_coords)):
        flip_df['Y-value'] = np.where(flip_df['Y-axis'] == y_coords[i], y_values[i], flip_df['Y-value'])

    flip_df['X-value'] = np.nan
    x_coords = sorted(flip_df['X-axis'].unique())

    for i in range(len(x_coords)):
        flip_df['X-value'] = np.where(flip_df['X-axis'] == x_coords[-(i+1)], i+1, flip_df['X-value'])

    flip_df['X-value'] = flip_df['X-value'].astype('int')
    tid = flip_df['Y-value'] + flip_df['X-value'].astype('str')
    flip_df['tid'] = tid

    return flip_df


def find_neighbors(tf_world_df, tid):
    y_values = ['DDD', 'CCC', 'BBB', 'AAA', 'ZZ', 'YY', 'XX', 'WW', 'VV', 'UU', 'TT', 'SS', 'RR', 'QQ', 'PP', 'OO',
                'NN', 'MM', 'LL', 'KK', 'JJ', 'II', 'HH', 'GG', 'FF', 'EE', 'DD', 'CC', 'BB', 'AA', 'Z', 'Y', 'X',
                'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D',
                'C', 'B', 'A']
    x_value_max = 33
    tid_location_df = tf_world_df.loc[tf_world_df['tid'] == tid, ['Y-value', 'X-value']]

    # searching for vertical neighbors two indexes up and two indexes down.
    vertical_neighbors = []
    if tid_location_df['Y-value'].values == 'A':
        vertical_neighbors = ['B', 'C']
    elif tid_location_df['Y-value'].values == 'B':
        vertical_neighbors = ['A', 'C', 'D']
    elif tid_location_df['Y-value'].values == 'DDD':
        vertical_neighbors = ['BBB', 'CCC']
    elif tid_location_df['Y-value'].values == 'CCC':
        vertical_neighbors = ['AAA', 'BBB', 'DDD']
    else:
        y_index = y_values.index(tid_location_df['Y-value'].values)
        indices_to_access = [y_index + 2, y_index + 1, y_index - 1, y_index - 2]

        vertical_mapping = map(y_values.__getitem__, indices_to_access)
        vertical_neighbors = list(vertical_mapping)

    tiddies = []
    for vertical_neighbor in vertical_neighbors:
        neighbor_index = y_values.index(vertical_neighbor)
        y_index = y_values.index(tid_location_df['Y-value'].values)
        horizontal_neighbors = []
        if tid_location_df['X-value'].values == 1:
            horizontal_neighbors = [1, 2]
            if abs(neighbor_index - y_index) == 1:
                tiddies.append(vertical_neighbor + str(horizontal_neighbors[1]))
            else:
                tiddies.append(vertical_neighbor + str(horizontal_neighbors[0]))
        elif tid_location_df['X-value'].values == x_value_max:
            horizontal_neighbors = [32, 33]
            if abs(neighbor_index - y_index) == 1:
                tiddies.append(vertical_neighbor + str(horizontal_neighbors[0]))
            else:
                tiddies.append(vertical_neighbor + str(horizontal_neighbors[1]))
        else:
            x_value = tid_location_df['X-value'].values
            horizontal_neighbors = [x_value - 1, x_value, x_value + 1]
            if abs(neighbor_index - y_index) == 1:
                tiddies.append(vertical_neighbor + str(horizontal_neighbors[0][0]))
                tiddies.append(vertical_neighbor + str(horizontal_neighbors[2][0]))
            else:
                tiddies.append(vertical_neighbor + str(horizontal_neighbors[1][0]))

    neighbors_df = pd.DataFrame()
    for tid in tiddies:
        neighbors_df = pd.concat([neighbors_df, tf_world_df.loc[tf_world_df['tid'] == tid]], ignore_index=True)

    return neighbors_df
