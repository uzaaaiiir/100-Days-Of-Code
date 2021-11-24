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
    Shuffles the deck before returning.
    '''
    deck = []
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'K', 'Q', 'A']
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    for rank in ranks:
        for suit in suits:
            deck.append(rank+suit)
    random.shuffle(deck)
    return deck 


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
def blackjack(deck, player, dealer):
    checkScores = check(player, dealer)
    print(f"\tYour card: {player}, current score: {checkScores[1]}")
    print(f"\tComputer's first card: {dealer[0]}")

    if checkScores[1]==21 and checkScores[2]==21:
        print("Draw!")
        return
    elif checkScores[1]==21:
        print("You win!")
        return
    elif checkScores[2]==21:
        print("You lose. Dealer wins!")
        return
    elif checkScores[1]>21:
        print("You lose! You bust.")
        return
    elif checkScores[2]>21:
        print("You win! Dealer bust.")
        return


    continueDeal = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
    flag = True 
    while True:
        if continueDeal=='y':
            player.append(deck.pop())
            flag = False 
            blackjack(deck, player, dealer)
        elif continueDeal=='n':
            dealer.append(deck.pop())
            flag = False
            blackjack(deck,player,dealer)
        else:
            print("Please enter 'y' or 'n'.")
    
flag = True 
while flag:
    playGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
    if playGame == 'y':
        print("\033c")
        blackjackArt()
        deck = makeDeck()
        player = [deck.pop(), deck.pop()]
        dealer = [deck.pop(), deck.pop()]
        blackjack(deck, player, dealer)
    elif playGame == 'n':
        print("Thank you for playing. Goodbye!")
        flag= False 
    else:
        print("Please enter 'y' or 'n'.")