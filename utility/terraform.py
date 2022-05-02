import pandas as pd
import numpy as np
from utility import cartographer


def dark_water():
    return 'ocean'


def light_water(tf_world_df, tid):
    tile_neighbors = cartographer.find_neighbors(tf_world_df, tid)


def terraform_world(world_df):
    tf_world_df = world_df
    tf_world_df['RegionType'] = np.nan
    for tid in tf_world_df['tid']:
        type_value = tf_world_df.loc[tf_world_df['tid'] == tid, 'Type'].values
        tile_type = type_value[0][2:-1]

        if tile_type == 'dark_water':
            tf_world_df.loc[tf_world_df['tid'] == tid, 'RegionType'] = dark_water()
