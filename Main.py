import GlobalVariables

def(main):
    print(GlobalVariables.GameTitle)
    
def Names():
    PlayerName = input('What is your name player?')
    Pip = print('Pip')
    print(f'Unknown Voice: Welcome to the game {PlayerName}. \I am your friend and guide, {Pip}. \nAs you see I appear human like you, but no one else can see me. I can feel the affects of the real world though. \nIt is time to begin our journey! I will see you soon. \nGood luck!')

def CurrentPlaythrough():
    print(f'Player Name: {PlayerName}')
    print(f'Current Stats: GlobalVariables.PowersDict')
    
def StartNew(): #starts the game by starting the game at the Introductio.py file
