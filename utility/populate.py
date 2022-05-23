import pandas as pd
import numpy as np
import random


def generate_name():
    name = ''
    beginning = ['', '', '', '', 'a', 'be', 'de', 'el', 'fa', 'jo', 'ki', 'la', 'ma', 'na', 'o', 'pa', 're', 'si', 'ta',
                 'va']
    middle = ['bar', 'ched', 'dell', 'far', 'gran', 'hal', 'jen', 'kel', 'lim', 'mor', 'net', 'penn', 'quil', 'rond',
              'sark', 'shen', 'tur', 'vash', 'yor', 'zen']
    end = ['', 'a', 'ac', 'ai', 'al', 'am', 'an', 'ar', 'ea', 'el', 'er', 'ess', 'ett', 'ic', 'id', 'il', 'in', 'is',
           'or', 'us']
    beginning_index = random.randint(0, (len(beginning) - 1))
    middle_index = random.randint(0, (len(middle) - 1))
    end_index = random.randint(0, (len(end) - 1))

    name = beginning[beginning_index] + middle[middle_index] + end[end_index]
    return name


def generate_tavern():
    tavern_dict = {}
    die_roll = random.randint(1, 20)
    first_part = ['The Silver', 'The Golden', 'The Staggering', 'The Laughing', 'The Prancing', 'The Gilded',
                  'The Running', 'The Howling', 'The Slaughtered', 'The Leering', 'The Drunken', 'The Leaping',
                  'The Roaring', 'The Frowning', 'The Lonely', 'The Wandering', 'The Mysterious', 'The Barking',
                  'The Black', 'The Gleaming']
    second_part = ['Eel', 'Dolphin', 'Dwarf', 'Pegasus', 'Pony', 'Rose', 'Stag', 'Wolf', 'Lamb', 'Demon', 'Goat',
                   'Spirit', 'Horde', 'Jester', 'Mountain', 'Eagle', 'Satyr', 'Dog', 'Spider', 'Star', 'Pickle',
                   'Frustration', 'Goblin']
    return


def generate_factions():
    return


def factor_faction_strength():
    return


def generate_cities_and_villages(tf_world_df, political_df):
    region_type_value = {
        'ocean': 0,
        'sea': 1,
        'lake': 1,
        'desert': 1,
        'hills': 3,
        'grasslands': 2,
        'mountains': 2,
        'arctic': 1,
        'swamp': 1,
        'forest': 3
    }
    region_type_counts = tf_world_df['RegionType'].value_counts()
    population_support_value = 0
    for key in region_type_counts.keys():
        if key in region_type_value.keys():
            population_support_value = population_support_value + (region_type_counts[key] * region_type_value[key])

    general_density = 40  # this density is people per square miles
    hex_square_miles = 32  # Square miles for a six mile hex
    population_support_value = population_support_value * general_density * hex_square_miles

    m_rng = random.randint(2, 16) + 10
    largest_city_population = int(np.sqrt(population_support_value) * m_rng) * 6
    largest_city_name = generate_name()

    percent_of_largest = random.randint(5, 8) * .1
    second_city_population = int(largest_city_population * percent_of_largest)
    second_city_name = generate_name()

    percent_of_previous = random.randint(2, 8) * .05
    next_city = second_city_population * percent_of_previous
    while next_city >= 8000:
        next_city_name = generate_name()
        percent_of_previous = random.randint(2, 8) * .05
        next_city = next_city * percent_of_previous


    return


def place_city():
    return


def place_town():
    return


def place_village():
    return


def generate_dungeons():
    return


def draw_political_map(tf_world_df):
    political_df = pd.DataFrame()
    political_df = pd.concat([political_df, tf_world_df['tid']], ignore_index=True)
    political_df['CityTown'] = ''
    political_df['Population'] = np.nan
    political_df['CivTags'] = ''
    political_df['Factions'] = []
    political_df['Dungeon'] = ''
    political_df['DungeonTags'] = ''
    political_df['Taverns'] = []
    political_df['Demographics'] = {}
    political_df['Leadership'] = ''

    return


def update_faction():
    return


def update_faction_strength():
    return


def update_city():
    return


def update_village():
    return


def update_dungeon():
    return
