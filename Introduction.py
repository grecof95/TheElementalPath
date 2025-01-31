intro = print(
    f'You wake up in your bed. "{Pip}: {PlayerName}!" It is me, {Pip}! \nToday is the day we must venture out to find the magic needed to save your town. \nLet us head out the door.')

def Start():
    def St():
        ready = input(f'{Pip:} Are you ready {PlayerName}?').lower()
        return ready
    
    response = St()
    
    while response != 'yes':
        print('{Pip}: We must leave soon! The town is counting on us!')
        response = St()
        if response == 'yes':
            print(f'{Pip} Great! Let us begin our journey! \nThe town is counting on us!')
            break

Start()