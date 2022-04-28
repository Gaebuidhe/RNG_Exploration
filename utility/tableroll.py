import pandas as pd
import random as rng

## this turns the chance list into a more searchable form, Table_Roll uses it
def enumerator(list):
    low = int(list[0])
    high = int(list[-1])
    resultlist = " "
    for i in range (low,(high + 1)):
        resultlist += str(i)
        resultlist += " "
    
    return(resultlist)
        

##feed this a CSV table with columns Chance, Value. It will roll on chance and return the associated value.

def Table_Roll(table_name):
    #read the table
    df_table = pd.read_csv(('utility\\rollable tables\\' + table_name + '.csv'), encoding = 'unicode_escape');
    ## the - in beyond's tables is a special character. Make sure it's all strings, remove any -'s, convert to arrays
    df_table['Chance'] = df_table['Chance'].astype(str)
    df_table['Chance'] = df_table['Chance'].str.replace('–',' ')
    df_table['Chance'] = df_table['Chance'].str.replace('-',' ')
    df_table['Chance'] = df_table['Chance'].str.split(' ')
    ## define the outer bounds of the roll, this method allows for 3d6 rolls. Chance will be more random than with dice.
    table_upper = df_table.iloc[-1,0]
    table_upper = table_upper[-1]
    
    table_lower = df_table.iloc[0,0]
    table_lower = table_lower[0]
    
    
    roll = rng.randint(int(table_lower),int(table_upper))
    
    ## use enumerator to turn th lists back into searchable strings
    df_table['Chance'] = df_table['Chance'].apply(enumerator)
    
    ## enumrator creates spaces around the possible results, this uses that to find 5 but not 15
    roll_result = df_table.loc[df_table['Chance'].str.contains((" "+ str(roll) + " "))]
    roll_result = roll_result.iloc[0,1]
    
    ##return the value associated with the roll
    return(roll_result);
    

    
    
##print(Table_Roll('10 gp gemstones'));
