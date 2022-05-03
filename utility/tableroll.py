import pandas as pd
import random as rng
import re

## this turns the chance list into a more searchable form, Table_Roll uses it
def enumerator(list):
    low = int(float(list[0]))
    high = int(float(list[-1]))
    resultlist = " "
    for i in range (low,(high + 1)):
        resultlist += str(i)
        resultlist += " "
    
    return(resultlist)
        
def RollCheck(ingested_string):
    ##polish the ingested string, standardizing the formating of +/-
    ingested_string = ingested_string.replace('+', " + ")
    ingested_string = ingested_string.replace('-'," - ")
    ingested_string = ingested_string.replace('  '," ")
    ## break the string into a list so it can be examined for rolls
    Istring = ingested_string.split(' ')
    dicetest = []
    rolls = 0
    rollsum = 0
    ##for testing purposes, this tracks individual rolls
    ##rollsumtrack = []
    ingested_length = range(len(Istring))
    for i in ingested_length:
        ##editing putting the +/- together in the () can change length, break if i would exceed current length
        if i not in ingested_length: break
        ##look for a d, if there is one split that value and check for numbers
        if Istring[i].find('d') != -1:
            dicetest = Istring[i].split('d')
            if dicetest[-1].isnumeric():
                ##in a roll like "d10 stuff" the first value will be ''
                if dicetest[0] != '':
                    ##if there is a number of dice, rolll that many times, summing, otherwise roll just the one
                    while rolls < int(dicetest[0]):
                        rollsum = rollsum + rng.randint(1,int(dicetest[-1]))
                        ##the below is for testing, it tracks individual rolls
                        ##rollsumtrack.append(rollsum)
                        rolls = rolls + 1
                else:
                    rollsum = rng.randint(1,int(dicetest[-1]))
                ## check for +/-, apply them, squish them into the () and delete the leftovers
                if Istring[i+1] == '+':
                    rollsum = rollsum + int(Istring[i+2])
                    Istring[i] = (Istring[i] + Istring[i+1] + Istring[i+2])
                    del Istring[i+1]
                    del Istring[i+1]
                    ingested_length = range(len(Istring))
                elif Istring[i+1] == '-':
                    rollsum = rollsum - int(Istring[i+2])
                    Istring[i] = (Istring[i] + Istring[i+1] + Istring[i+2])
                    del Istring[i+1]
                    del Istring[i+1]
                    ingested_length =  range(len(Istring))
                Istring[i] = (str(rollsum) + '('+ Istring[i]+')')
            ## set these to 0 to be use again for multiple rolls in one string
            rollsum = 0
            rolls = 0
        
    Istring = ' '.join(Istring)
    return Istring;
            
                        
                
    
    
    
    
##feed this a CSV table with columns Chance, Value. It will roll on chance and return the associated value.

def Table_Roll(table_name):
    #read the table
    df_table = pd.read_csv(('utility\\rollable tables\\' + table_name + '.csv'), encoding = 'unicode_escape');
    ## the - in beyond's tables is a special character. Make sure it's all strings, remove any -'s, convert to arrays
    df_table['Chance'] = df_table['Chance'].astype(str)
    df_table['Chance'] = df_table['Chance'].str.replace('\x96',' ')
    df_table['Chance'] = df_table['Chance'].str.replace('–',' ')
    df_table['Chance'] = df_table['Chance'].str.replace('-',' ')
    df_table['Chance'] = df_table['Chance'].str.split(' ')
    df_table['Value'] = df_table['Value'].str.replace('\xa0', ' ')
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
    roll_result = RollCheck(roll_result)
    
    ##return the value associated with the roll
    return(roll_result);
    

    
    
print(RollCheck("d6-1"));
