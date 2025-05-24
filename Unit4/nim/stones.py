def pick_for_user():
    """Pick the number of stones for the user"""
    
    #Ask the user for the number of stones
    user_stones=0
    
    #Check that this number is either one or two and if not keeps asking user until we ger 1 or 2
    while not(user_stones==1 or user_stones==2):
        user_stones=int(input("How many stones do you want to pick up? (1 or 2)" + " "))
        
    #Return this number
    return user_stones

def pick_for_computer():
    """Pick the number of stones for the computer"""
    return 1
