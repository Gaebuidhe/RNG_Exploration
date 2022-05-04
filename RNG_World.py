#!/usr/bin/env python
##############################
# Created by Dia the GM
#
# https://github.com/Gaebuidhe/RNG_Exploration
##############################

import pandas as pd
import numpy as np
from utility import terraform as tf
from utility import cartographer as cg

import os
import argparse

from argparse import RawTextHelpFormatter

pd.options.mode.chained_assignment = None

parser = argparse.ArgumentParser(description='Process custom RNG requests and create exploration campaign.')

parser.add_argument('-s', '--seed', action="store", dest='seed', help='Seed being used to identify the world.')
subparser = parser.add_subparsers(title=" RNG_World Utilities",
                                  description="RNG World utilities available. This will include world building,"
                                              "geographical information, political information, and encounter building "
                                              "tools. DMs/GMs should utilize these tools and adjust as necessary to "
                                              "make an engaging world for the players to explore.",
                                  dest='utility')

full_build = subparser.add_parser("Full_Build", help="For flat runs of all maps, geographical map, or political map"
                                                     "(example: $ python .\\RNG_World.py -s 1491363712 Full_Build -a)")
full_build.add_argument('-a', '--all', action='store_true', help='Run full build on all maps')
full_build.add_argument('-g', '--geographical', action='store_true', help='Run full build on geographical map')
full_build.add_argument('-p', '--political', action='store_true', help='Run full build on political map')

adjust_geo = subparser.add_parser("Adjust_Geo",
                                  help="For Adjusting geographical features of the map (i.e. Region Type or Tags)")
adjust_geo.add_argument('-R', '--region_type', action="store", dest='region_type',
                        help="Region type to be used to update tile")
adjust_geo.add_argument('-r', '--region_tags', action="store", dest='region_tag', help="Region tags")
adjust_geo.add_argument('-a', '--add', action="store_true", help="Add region tags to tile")
adjust_geo.add_argument('-d', '--delete', action="store_true", help="Remove region tags from tile")
adjust_geo.add_argument('-t', '--tid', action="store", dest='tid', help="Tile to update")

args = parser.parse_args()

if args.seed is not None:
    print(f'Welcome to Jurassic Seed {args.seed}!')
    seed_location = f'map_pyde\\Examples\\csv\\{args.seed}.csv'
    raw_df = pd.read_csv(seed_location)
    flip_df = cg.set_tiddies(raw_df, 5)

    if args.utility == 'Full_Build':
        if args.all or args.geographical:
            terraform_csv = f'campaigns\\notes\\{args.seed}_geographical.csv'
            tf_world_df = tf.terraform_world(flip_df)
            tf_world_df.to_csv(terraform_csv, index=False)

        if args.all or args.political:
            political_csv = f'campaigns\\notes\\{args.seed}_political.csv'

    if args.utility == 'Adjust_Geo':
        print(args)
        region_type_list = ['ocean', 'sea', 'lake', 'desert', 'hills', 'grasslands', 'mountains', 'arctic', 'swamp',
                            'forest']
        geo_csv = f'campaigns\\notes\\{args.seed}_geographical.csv'
        tf_world_df = pd.read_csv(geo_csv)

        while args.tid is None:
            args.tid = input("Please Enter TID (i.e. DD20):")

        if args.region_type is not None:
            while args.region_type not in region_type_list:
                args.region_type = input(f'Please use one of the following Region Types: {region_type_list}\n')

            updated_world_df = tf.update_region_type(args.region_type, args.tid, tf_world_df)

