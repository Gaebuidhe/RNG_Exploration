import pandas as pd
import random as rng

## this turns the chance list into a more searchable form
def enumerator(list):
    low = int(list[0])
    high = int(list[-1])
    resultlist = " "
    for i in range (low,(high + 1)):
        resultlist += str(i)
        resultlist += " "
    
    return(resultlist)
        

def Table_Roll(table_name):
    #read the table
    df_table = pd.read_csv(('utility\\rollable tables\\' + table_name + '.csv'));
    ## the - in beyond's tables is a special character. Remove them and break any ranges into lists
    df_table['Chance'] = df_table['Chance'].str.replace('–',' ').replace('-',' ').str.split(' ')
    
    ## define the outer bounds of the roll
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
    

    
    
##print(Table_Roll('ruler traits'));
