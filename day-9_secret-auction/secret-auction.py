def art():
    logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
    '''
    print(logo)

def getName():
    '''(None)->str
    Function prompts the user for their name.
    Function returns the name.
    '''
    name = input("What is your name? ")
    return name

def getBid():
    '''(None)->number as a float
    Function prompts the user to enter a number as a bid in the auction. 
    Function returns the bid entered as a float.
    '''
    flag = True
    while flag: 
        try:
            bid = float(input("What's your bid? "))
            flag = False 
        except: 
            print("Please enter a number.")
    return bid

def secret_auction():
    '''(None)->dict
    Function prompts the user for the names and bids for the users in the auction.
    Function returns a dictionary with the users mapped to the bid made. 
    '''
    flag = True
    users = {}

    while flag:
        name = getName()
        bid = getBid()
        users[name]=bid 
        newUser = input("Are there any other bidders? Type 'yes' or 'no': ").lower().strip()
        if newUser=='yes':
            print("\033c")
        elif newUser=='no':
            print("\033c")
            flag=False
        elif newUser!='yes':
            print("Please enter 'yes' or 'no'.")
    return users 

def winnerOfBid(userInputs):
    '''(dict)->str
    Function takes a dictionary as input.
    Returns the user in the dictionary that has the highest value of the bid. 
    '''
    winner = ''
    max = 0 
    for bidder in userInputs:
        if userInputs[bidder]>max:
            max = userInputs[bidder]
            winner = bidder
    return winner

# main
art()
print("Welcome to the secret auction program.")
userInputs = secret_auction()
winner = winnerOfBid(userInputs)
for key in userInputs:
    print(f"{key}: {userInputs[key]}")
print(f"The winner of the auction is {winner}, with a bid of ${int(userInputs[winner])}.")