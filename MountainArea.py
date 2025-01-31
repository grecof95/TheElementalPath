#MountainArea Codes

import AreaEntrace
import GlobalVariables

#Mountain Bonus Prints current dictionary values. Adds 1 to Strength and Health
def MountainBonus():
    print(f'Your current stats are {PowersDict}. \nYou have been blessed with the Mountain bonus. \nYour stats will increase with a priority in strength and health.')
    
    PowersDict['Strength'] += 1
    PowersDict['Max Health'] += 1
    BonusStats()
    
    print(f'Your stats have been updated to {PowersDict}.')