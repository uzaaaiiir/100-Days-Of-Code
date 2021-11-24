import random

def blackjackArt():
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
        |  \/ K|                            _/ |                
        `------'                           |__/           
    """
    print(logo)

def makeDeck():
    '''(None)->list of str
    Function returns a list representing a deck of cards in the format (rank + suit)
    '''
    deck = []
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'K', 'Q', 'A']
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    for rank in ranks:
        for suit in suits:
            deck.append(rank+suit)
    return deck 

def deal2Cards(player1, player2, deck):
    '''(list,list)->None
    Function takes two lists representing the players cards and a deck.
    Deals two cards to each player and removes them from the deck.
    '''
    x1 = random.randint(0,len(deck)-1)
    player1.append(deck.pop(x1))
    x2 = random.randint(0,len(deck)-1)
    player1.append(deck.pop(x2))

    y1 = random.randint(0,len(deck)-1)
    player2.append(deck.pop(y1))
    y2 = random.randint(0,len(deck)-1)
    player2.append(deck.pop(y2))
    

def check(user1, user2):
    '''(list, list)->dict
    Function takes two lists representing the cards that each user has.
    Returns a dictionary of each user and their scores.
    '''
    cardValue = {
        '2': 2, '3': 3,
        '4': 4, '5': 5,
        '6': 6, '7': 7,
        '8': 8, '9': 9,
        'J': 10, 'Q': 10,
        'K': 10, 'A': [1,11]
    }
    player1Total = 0
    player2Total = 0

    for i in user1:
        if i[0]=='A':
            if player1Total + 11 > 21:
                player1Total = player1Total + cardValue[i[0]][0]
            else:
                player1Total = player1Total + cardValue[i[0]][1]
        else:
            player1Total = player1Total + cardValue[i[0]]
    for i in user2:
        if i[0]=='A':
            if player2Total + 11 > 21:
                player2Total = player2Total + cardValue[i[0]][0]
            else:
                player2Total = player2Total + cardValue[i[0]][1]
        else:
            player2Total = player2Total + cardValue[i[0]]    

    userDict = {
        1: player1Total,
        2: player2Total
    }
    return userDict

# main
def blackjack():
    deck = makeDeck()
    player1 = []
    player2 = []
    deal2Cards(player1, player2, deck)
    checkScores = check(player1, player2)

flag = True 
while flag:
    blackjackArt()
    playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
    if playGame == 'y':
        winner = blackjack()
    elif playGame == 'n':
        pass
    else:
        print("Please enter 'y' or 'n'.")