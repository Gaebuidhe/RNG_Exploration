import pandas as pd
import numpy as np


def find_neighbors(world_df, tid):
    y_values = ['DDD', 'CCC', 'BBB', 'AAA', 'ZZ', 'YY', 'XX', 'WW', 'VV', 'UU', 'TT', 'SS', 'RR', 'QQ', 'PP', 'OO',
                'NN', 'MM', 'LL', 'KK', 'JJ', 'II', 'HH', 'GG', 'FF', 'EE', 'DD', 'CC', 'BB', 'AA', 'Z', 'Y', 'X',
                'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D',
                'C', 'B', 'A']
    x_value_max = 33
    tid_location_df = tf_world_df.loc[tf_world_df['tid'] == tid, ['Y-value', 'X-value']]

    # searching for vertical neighbors two indexes up and two indexes down.
    vertical_neighbors = []
    if tid_location_df['Y-value'].value is 'A':
        vertical_neighbors = ['B', 'C']
    elif tid_location_df['Y-value'].value is 'B':
        vertical_neighbors = ['A', 'C', 'D']
    elif tid_location_df['Y-value'].value is 'DDD':
        vertical_neighbors = ['BBB', 'CCC']
    elif tid_location_df['Y-value'].value is 'CCC':
        vertical_neighbors = ['AAA', 'BBB', 'DDD']
    else:
        y_index = y_values.index(tid_location_df['Y-value'].value)
        indices_to_access = [y_index + 2, y_index + 1, y_index - 1, y_index - 2]

        vertical_mapping = map(y_values.__getitem__, indices_to_access)
        vertical_neighbors = list(vertical_mapping)

    tiddies = []
    for vertical_neighbor in vertical_neighbors:
        neighbor_index = y_values.index(vertical_neighbor)
        y_index = y_values.index(tid_location_df['Y-value'].value)
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
                tiddies.append(vertical_neighbor + str(horizontal_neighbors[0]))
                tiddies.append(vertical_neighbor + str(horizontal_neighbors[2]))
            else:
                tiddies.append(vertical_neighbor + str(horizontal_neighbors[1]))


def dark_water():
    return 'ocean'


def terraform_world(world_df):
    tf_world_df = world_df
    tf_world_df['RegionType'] = np.nan
    for tid in tf_world_df['tid']:
        type_value = tf_world_df.loc[tf_world_df['tid'] == tid, 'Type'].values
        tile_type = type_value[0][2:-1]

        if tile_type == 'dark_water':
            tf_world_df.loc[tf_world_df['tid'] == tid, 'RegionType'] = dark_water()
