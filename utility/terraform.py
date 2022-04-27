import pandas as pd
import numpy as np


def dark_water():
    return 'ocean'


def terraform_world(world_df):
    tf_world_df = world_df
    tf_world_df['RegionType'] = np.nan
    for tid in tf_world_df['tid']:
        temp_df = tf_world_df[tf_world_df['tid'] == tid]
        if temp_df['type'] == 'd'