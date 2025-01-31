import GlobalVariables
import Main

def LateGame():
    #checks the globalvariables

def EarlyGame():
    '''
    checks the globalvariables.py for each of the keys in the EarlyCompletedAreas 
    to be marked true or false. Any item marked as false will allow access to the associated area py file (WoodsArea.py, etc.)
    If any key is marked true, then that area is completed and a message will say you've finished this area and to select another area - 
    then rerun this script from the top. Once all items are marked True, a prompt will appear that you are ready for the late game
    then I can run the LateGame() function
    '''
    