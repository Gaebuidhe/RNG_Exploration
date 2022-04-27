##############################
# Created by Dia the GM
#
#
##############################

import pandas as pd
import numpy as np

import os
import argparse

parser = argparse.ArgumentParser(description='Process custom RNG requests and create exploration campaign.')

parser.add_argument('-s', '--seed', action="store", dest='seed', help='Seed being used to generate data')

args = parser.parse_args()

y_values = ['DDD', 'CCC', 'BBB', 'AAA', 'ZZ', 'YY', 'XX', 'WW', 'VV', 'UU', 'TT', 'SS', 'RR', 'QQ', 'PP', 'OO',
            'NN', 'MM', 'LL', 'KK', 'JJ', 'II', 'HH', 'GG', 'FF', 'EE', 'DD', 'CC', 'BB', 'AA', 'Z', 'Y', 'X',
            'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D',
            'C', 'B', 'A']

if args.seed is not None:
    print(f'Welcome {args.seed}')
    seed_location = f'map_pyde\\Examples\\csv\\{args.seed}.csv'
    raw_df = pd.read_csv(seed_location)
    bad_rows = 5
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

    save_csv = f'campaigns\\notes\\{args.seed}.csv'
    flip_df.to_csv(save_csv, index=False)

