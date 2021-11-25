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
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    for rank in ranks:
        for suit in suits:
            deck.append(rank+suit)
    random.shuffle(deck)
    return deck 

def dealCard(deck, user):
    '''(list, list)->list
    Function takes two inputs, one representing the deck of cards and one representing the cards a user has.
    The function returns the users cards with another card from the deck added to it.
    '''
    user.append(deck.pop())
    return user

def calculateScore(user):
    '''(list of str)->int
    Function takes a list representing a hand of cards.
    It returns the value of the score associated with the hand.
    Precondition: user is a list with each item being of the format ['rank+suit']
    '''
    scoreMap = {
        2: ['2\u2660', '2\u2661', '2\u2662', '2\u2663'],
        3: ['3\u2660', '3\u2661', '3\u2662', '3\u2663'],
        4: ['4\u2660', '4\u2661', '4\u2662', '4\u2663'],
        5: ['5\u2660', '5\u2661', '5\u2662', '5\u2663'],
        6: ['6\u2660', '6\u2661', '6\u2662', '6\u2663'],
        7: ['7\u2660', '7\u2661', '7\u2662', '7\u2663'],
        8: ['8\u2660', '8\u2661', '8\u2662', '8\u2663'],
        9: ['9\u2660', '9\u2661', '9\u2662', '9\u2663'],
        10: ['10\u2660', '10\u2661', '10\u2662', '10\u2663', 'J\u2660', 'J\u2661', 'J\u2662', 'J\u2663',
        'Q\u2660', 'Q\u2661', 'Q\u2662', 'Q\u2663', 'K\u2660', 'K\u2661', 'K\u2662', 'K\u2663'],
        11: ['A\u2660', 'A\u2661', 'A\u2662', 'A\u2663'],
    }
    score = 0 
    for i in scoreMap:
        for j in user:
            if j in scoreMap[i] and i!=11:
                score = score + i
            elif j in scoreMap[i] and i==11:
                if score + i >21:
                    score = score + 1
                else:
                    score = score + 11
    if score==21: return 0
    return score

def compareScore(scorePlayer, scoreDealer):
    if scorePlayer==21 and scoreDealer==21:
        print("Draw!")
        return False
    elif scorePlayer==21:
        print("Congratulations, you win!")
        return False
    elif scoreDealer==21:
        print("Blackjack! Dealer wins.")
        return False
    elif scorePlayer>21:
        print("You bust! Dealer wins.")
        return False
    elif scoreDealer>21:
        print('Dealer busts! You win.')
        return False
    else:
        return True 

def pickAnotherCard():
    flag = True
    while flag:
        inputUser = input("Type 'y' to get another card, type 'n' to pass: ")
        if inputUser not in ['y','n']:
            print("Please enter 'y' or 'n' only.")
        else: 
            flag = False
    return inputUser  

def blackjack():
    deck = makeDeck()
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]
    scorePlayer = calculateScore(player)
    scoreDealer = calculateScore(dealer)

    print(f"\tYour cards: {player}, current score: {scorePlayer}")
    print(f"\tComputer's first card: {dealer[0]}")

    flag = compareScore(scorePlayer, scoreDealer)

    while flag:
        userInput = pickAnotherCard()
        if userInput=='y':
            player.append(deck.pop())
            scorePlayer = calculateScore(player)
            print(f"\tYour cards: {player}, current score: {scorePlayer}")
            print(f"\tComputer's first card: {dealer[0]}")
            flag = compareScore(scorePlayer, scoreDealer)
        elif userInput=='n':
            dealer.append(deck.pop())
            scoreDealer = calculateScore(dealer)
            print(f"\tYour cards: {player}, current score: {scorePlayer}")
            print(f"\tComputer's first card: {dealer[0]}")
            flag = compareScore(scorePlayer, scoreDealer)
    print(f"\tYour final hand: {player}, final score: {scorePlayer}")
    print(f"\tComputer's final hand: {dealer}, final score: {scoreDealer}")


# main
flag = True
while flag:
    continuePlaying = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
    if continuePlaying == 'y': 
        print("\033c")
        blackjackArt()
        blackjack()
    elif continuePlaying=='n':
        print("Thank you for playing. Have a good day!")
        flag = False
    else:
        print("Please enter 'y' or 'n'")