import game_data
import random

def higherlowerArt():
    art = '''
     _   _ _       _                 _                          
    | | | (_) __ _| |__   ___ _ __  | |    _____      _____ _ __ 
    | |_| | |/ _` | '_ \ / _ \ '__| | |   / _ \ \ /\ / / _ \ '__|
    |  _  | | (_| | | | |  __/ |    | |__| (_) \ V  V /  __/ |   
    |_| |_|_|\__, |_| |_|\___|_|    |_____\___/ \_/\_/ \___|_|   
            |___/                                               
    '''
    print(art)

def vs():
    vsArt = '''
     __   _____ 
     \ \ / / __|
      \ V /\_ _\\
       \_/ |___/
    '''
    print(vsArt)

def distinctOption(optionsAmount, optionA):
    '''(int, dict)->dict
    Takes a dictionary representing a person and the number of items in a list of dicts.
    Returns a random item in the list of dicts that is not the same as optionA.
    '''
    optionBIndex = random.randint(0, optionsAmount-1)
    optionB = game_data.data[optionBIndex]
    while optionB==optionA:
        optionB = game_data.data[random.randint(0, optionsAmount-1)]
    return optionB
    
def checkScore(userChoice, answer, score):
    '''(str, list, int)->bool
    Functions takes as input a string representing the users choice and a list represent the correct answer(s).
    Takes as input the current score.
    Checks if the userchoice is in the list of correct answers.
    Returns True of the userchoice is a correct answer, and prints the updated score.
    If the userchoice is not a correct answer, returns False, prints the current score.
    Preconditions: userChoice is str of a single character, answer is a list of the correct answers. Score is a non-negative int. 
    '''
    if userChoice in answer:
        print("\033c")
        higherlowerArt()
        print(f"You're right! Current score: {score + 1}")
        return True

    elif userChoice not in answer:
        print("\033c")
        print(f"Sorry, that's wrong. Final score: {score}")
        return False

def checkAnswer(optionA, optionB):
    '''(dict, dict)->list of str 
    Takes two dictionaries as input. Returns which dictionary has a higher 'follower_count' as a list of str. 
    Preconditions: optinoA and optionB are represented as dictionaries.
    '''
    answer = []
    if optionA['follower_count'] > optionB['follower_count']:
        answer=['A']
    elif optionA['follower_count'] < optionB['follower_count']:
        answer=['B']
    else:
        answer=['A', 'B']
    return answer

def userInput():
    '''(None)->str
    Function prompts the user to enter 'A' or 'B'.
    Checks if the user enters a correct value, returns the str. 
    '''
    flag = True
    while flag:
        userChoice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
        if userChoice in ['A', 'B']:
            flag = False
    return userChoice 

# main

score = 0 
optionsAmount = len(game_data.data)

# Set initial Options 
optionAIndex = random.randint(0, optionsAmount-1)
optionA = game_data.data[optionAIndex]
optionB = distinctOption(optionsAmount, optionA)

# Introduction
print(optionA, '\n', optionB)
print("\033c")
higherlowerArt()

# Game 
flag = True 
while flag:
    # Print Options 
    print(f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}.")
    vs()
    print(f"Against B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}.")

    # Get user choice and makes sure the input is valid 
    userChoice = userInput()

    # Checks what the correct answer is from the two options 
    answer = checkAnswer(optionA, optionB)
    
    # Checks the score, sees if user has correct or wrong answer, dispays score
    flag = checkScore(userChoice, answer, score)

    # Sets new options for next round, updates score
    if flag == True:
        score += 1
        optionA = optionB
        optionB = distinctOption(optionsAmount, optionA)

print("Game over!")


    

