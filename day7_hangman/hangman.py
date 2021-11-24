import random

def hangman_art():
    '''(None)->None
    Prints a hangman greeting ASCII art.
    '''
    print('''
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                       
    ''')

def ascii_name_plaque(name):
    '''(str)->None
    Takes a name as an input, prints out a name plaque
    Preconditions: Name is a string, any quotes in the name must be single quotes
    '''
    length = len(name)
    print(5*"*" + length*('*') + 5*"*")
    print("*" + 4*" " + length*" " + 4*" " + "*")
    print("*" + "  "+ "__" + name + "__" + "  " + "*")
    print("*" + 4*" " + length*" " + 4*" " + "*")
    print(5*"*" + length*('*') + 5*"*")

def randomWord():
    '''(None)->str
    Function gets input of the category from the user.
    Returns a randomly generated word from the category chosen by the user.  
    '''
    animals = ['cat', 'dog', 'snake', 'bear', 'bat', 'bee', 'deer', 'duck',
    'goose', 'dove', 'tiger', 'lion', 'monkey', 'spider', 'squirrel', 'bird',
    'elephant', 'falcon', 'butterfly', 'ferret', 'guinea pig']
    food = ['fish', 'apple', 'pizza', 'burger', 'chicken', 'sandwich', 'rice'
    'cheese', 'pie', 'icecream', 'chocolate', 'chips', 'corn', 'noodles', 
    'bread', 'spaghetti', 'macaroni', 'fries', 'cookies', 'hashbrown', 'sushi']
    movies = ['Harry Potter', 'Batman', 'Suicide Squad', 'Black Panther',
    'Black Widow', 'Spiderman', 'Thor', 'The Notebook', 'Titanic', '21 Jumpstreet']
    sports = ['badminton', 'baseball', 'basketball', 'bowling', 'cycling', 'dodgeball'
    'fencing', 'football', 'golf', 'boxing', 'hockey', 'rowing', 'rugby', 'soccer',
    'skiing', 'snowboarding', 'swimming', 'tennis', 'volleyball', 'wresting']
    flag=True

    while flag:
        try:
            category = int(input("Please enter a category to start guessing: \n1 for Animals\n2 for Food\n3 for Movies\n4 for Sports\n"))
            if category in [1,2,3,4]:
                flag = False
            else:
                print("Please only enter numbers in 1, 2, 3, or 4.")
                print()
        except:
            print('Please enter a number.')
            print()
    
    if category==1:
        word = random.choice(animals)
    elif category==2:
        word = random.choice(food)
    elif category==3:
        word = random.choice(movies)
    elif category==4:
        word = random.choice(sports)
    return word

def getInput():
    '''(None)->str
    Function gets input from the user. The input is a letter guessed for the word.
    Returns the letter.
    '''
    letter = input("Enter a letter: ").lower().strip()
    if len(letter)!=1:
        print("Invalid input. Please enter a single character.")
        getInput()
    return letter

def listToString(n):
    '''(list of str)->str
    Function takes a list of strings as input.
    Concatenates the items of the list into a single string.
    Returns the string to the user.
    Preconditions: The input, n, is a list of strings.
    '''
    s = ''
    for i in range(len(n)):
        s = s + n[i]
    return s

def numberOfLetters(n):
    '''(str)->number or str
    Function takes a string as input, n. It computes the number of characters that are '_' in the string.
    Returns the number of characters that are '_'.
    '''
    count = 0
    for i in n:
        if i == '_':
            count+=1
    if count > 0:
        return count
    elif count==0:
        return 'no letters'

HANGMAN_PIC = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Main

# Greet user 
hangman_art()
print()
name = input("Welcome! What's your name?\n")
print()
ascii_name_plaque(name + ", welcome to the hangman game!")
print()

# Program Variables
word = randomWord()
blank = []
tempWord=''
lives = 6

# Creates blank 
for i in range(len(word)):
    if word[i]==' ':
        blank.append(' ')
    else:
        blank.append('_')
print(HANGMAN_PIC[0])
print("Try to guess the word right and save the hangman!")
print(f"Your word has {len(blank)} letters: {listToString(blank)}")
print()

# User Guesses
while '_' in blank and lives>0:
    letter = getInput()
    # If User guessess correct letter 
    if letter in word:
        print("You guessed correctly.")
        # Replaces the letter from the underscore 
        if letter in blank:
            print("But...you already guessed this before!")
        else:
            for i in range(len(word)):
                if word[i]==letter:
                    blank[i]=letter
        # Number of letters left to guess
        print(f"You have {numberOfLetters(blank)} left to guess: {listToString(blank)}")
        print(HANGMAN_PIC[6-lives])
        print()
    # If user guesses wrong, reduces lives
    else:
        lives = lives - 1
        print(f"You guessed {letter}, that's not in the word.")
        print(f"You lost a life. You now have {lives} lives.")
        print(f"You have {numberOfLetters(blank)} left to guess: {listToString(blank)}")
        print(HANGMAN_PIC[6-lives])
        print()

# End Game 
if lives==0:
    print(f"You lost! The correct word was {word}")
    print(f"That's ok, {name}, you can try again.")
elif '_' not in blank:
    print("Congratulations, you won!")