import pandas as pd
import numpy as np
import random

from utility import cartographer

pd.options.mode.chained_assignment = None



def dark_water():
    return 'ocean'



def light_water(tile_neighbors):
    if " 'dark_water'" in tile_neighbors['Type'].values:
        return 'sea'
    else:
        return 'lake'


def sand():
    return 'desert'


def grass(tile_neighbors):
    die_cast = random.randint(1, 100)
    type_counts = tile_neighbors['Type'].value_counts()
    mountain_count = 0
    if " 'rocky'" in type_counts.keys():
        mountain_count = type_counts[" 'rocky'"]

    if die_cast >= (76 - (10 * mountain_count)):
        return 'hills'
    else:
        return 'grasslands'


def rocky():
    return 'mountains'


def snowy():
    return 'arctic'


def dark_grass(tile_neighbors):
    die_cast = random.randint(1, 100)
    type_counts = tile_neighbors['Type'].value_counts()
    water_count = 0
    if " 'water'" in type_counts.keys():
        water_count = water_count + type_counts[" 'water'"]

    if " 'dark_water'" in type_counts.keys():
        water_count = water_count + type_counts[" 'dark_water'"]

    if die_cast >= (91 - (10 * water_count)):
        return 'swamp'
    else:
        return 'forest'


def regional_tags(tile_neighbors, tid, tf_world_df):
    region_tags = ''
    type_counts = tile_neighbors['Type'].value_counts()
    tid_df = tf_world_df.loc[tf_world_df['tid'] == tid]
    if " 'water'" in type_counts.keys() or " 'dark_water'" in type_counts.keys():
        if tid_df['Type'].values in [" 'dark_grass'", " 'grass'", " 'sand'", " 'rocky'", " 'snowy'"]:
            region_tags = region_tags + 'coastal'

    if tid_df['Type'].item() == " 'rocky'":
        die_cast = random.randint(1, 100)
        if die_cast >= 96 and region_tags == '':
            region_tags = region_tags + 'volcano'
        elif die_cast >= 96 and region_tags != '':
            region_tags = region_tags + ',volcano'

    underdark_die_cast = random.randint(1, 100)
    if underdark_die_cast >= 96 and region_tags == '':
        region_tags = region_tags + 'underdark entrance'
    elif underdark_die_cast >= 96 and region_tags != '':
        region_tags = region_tags + ',underdark entrance'

    return region_tags



def terraform_world(world_df):
    tf_world_df = world_df
    tf_world_df['RegionType'] = ''
    tf_world_df['RegionTags'] = ''
    for tid in tf_world_df['tid']:

        tile_neighbors = cartographer.find_neighbors(tf_world_df, tid)

        type_value = tf_world_df.loc[tf_world_df['tid'] == tid, 'Type'].values
        tile_type = type_value[0][2:-1]

        if tile_type == 'dark_water':
            tf_world_df.loc[tf_world_df['tid'] == tid, 'RegionType'] = dark_water()

        if tile_type == 'water':
            tf_world_df.loc[tf_world_df['tid'] == tid, 'RegionType'] = light_water(tile_neighbors)

        if tile_type == 'sand':
            tf_world_df.loc[tf_world_df['tid'] == tid, 'RegionType'] = sand()

        if tile_type == 'grass':
            tf_world_df.loc[tf_world_df['tid'] == tid, 'RegionType'] = grass(tile_neighbors)

        if tile_type == 'dark_grass':
            tf_world_df.loc[tf_world_df['tid'] == tid, 'RegionType'] = dark_grass(tile_neighbors)

        if tile_type == 'rocky':
            tf_world_df.loc[tf_world_df['tid'] == tid, 'RegionType'] = rocky()

        if tile_type == 'snowy':
            tf_world_df.loc[tf_world_df['tid'] == tid, 'RegionType'] = snowy()

        tf_world_df.loc[tf_world_df['tid'] == tid, 'RegionTags'] = regional_tags(tile_neighbors, tid, tf_world_df)

    return tf_world_df


def update_region_type(region_type, tid, tf_world_df):
    update_df = tf_world_df
    update_df.loc[update_df['tid'] == tid, 'RegionType'] = region_type
    return update_df


def add_region_tags(region_tags, tid, tf_world_df):
    update_df = tf_world_df
    current_tags = update_df.loc[update_df['tid'] == tid, 'RegionTags'].values[0]
    if current_tags == '':
        new_tags = region_tags
    else:
        new_tags = current_tags + ',' + region_tags
    update_df.loc[update_df['tid'] == tid, 'RegionTags'] = new_tags
    return update_df


def delete_region_tags(region_tags, tid, tf_world_df):
    update_df = tf_world_df
    old_tags = update_df.loc[update_df['tid'] == tid, 'RegionTags'].values
    tags = old_tags[0].split(',')
    remove_tags = region_tags.split(',')
    for tag in remove_tags:
        if tag in tags:
            tags.remove(tag)

    new_tags = ','.join(tags)
    update_df.loc[update_df['tid'] == tid, 'RegionTags'] = new_tags
    return update_df

