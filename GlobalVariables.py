#Global Variables

#Game Title
GameTitle = 'The Elemental Path'

#Stats
PowersDict = {
    'Strength': 1,
    'Magic': 1,
    'Endurance': 1,
    'Speed': 1,
    'Max Health': 10
}

Health = 10

def HealCurrentHealth():
    CurrentHealth = PowersDict['Health']
    return CurrentHealth
print(f'Your health has been fully restored. Your health is back to {HealCurrentHealth}.')

#Check stats
def CheckStats():
    print(PowersDict)
    
def StatsList():
    StatsList = [None, ]
    for key in PowersDict:
        StatsList.insert(key)
        return StatsList
    print(StatsList)

#Experience Points Bank that will be used to update PowerDict stats
ExpPoints= 0

def BonusStats():
    for key in PowersDict:
        PowersDict[key: +1]
        break

#Upgrade Point - If choose to not to upgrade, you won't be able to until the next upgrade point
def NormalStatUpgrade():
    print(f'Welcome to the upgrade point. \nYou have the option to upgrade your stats. \nYou can choose any of your stats. You will also be healed.')
    
    if ExpPoints > 0:
        StatUpgradeChoice = input(f'Which of these stats would you like to upgrade? {StatsList} \nType none if you do not want to upgrade and save your stat points for later.')
        while StatUpgradeChoice not in StatsList: 
            print('You must choose a valid stat to upgrade or type none to skip upgrade point.')
            StatUpgradeChoice
    else:
        print('You do not have enough experience points to upgrade your stats. Better luck next time')
        
    HealCurrentHealth()
    print(f'Your health has been restored to {HealCurrentHealth}.')
    print(f'Your stats have been updated to {PowersDict}.')

EarlyCompletedAreas = {
    'Woods': False,
    'Mountains': False,
    'Sea': False,
}

LateCompletedAreas = {
    'Bonus Dimension': False,
    'Final Dungeon': False
}