#SeaArea

import GlobalVariables

#Sea Bonus Prints current dictionary values. Adds 1 to Magic and Health
def SeaBonus():
    print(f'Your current stats are {PowersDict}. \nYou have been blessed with the Sea bonus. \nYour stats will increase with a priority in endurance and health.')
    
    PowersDict['Magic'] += 1
    PowersDict['Max Health'] += 1
    BonusStats()
    
    print(f'Your stats have been updated to {PowersDict}.')