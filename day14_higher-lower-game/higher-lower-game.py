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
    optionBIndex = random.randint(0,optionsAmount-1)
    optionB = game_data.data[optionBIndex]
    while optionB==optionA:
        optionB = game_data.data[random.randint(0,optionsAmount-1)]
    return optionB
    
    

optionsAmount = len(game_data.data)
score = 0 
optionAIndex = random.randint(0,optionsAmount-1)
optionA = game_data.data[optionAIndex]
optionB = distinctOption(optionsAmount, optionA)
print(optionA, '\n', optionB)

flag = True 
while flag:
    print("\033c")
    higherlowerArt()
    print(f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}")
    vs()
    print(f"Against B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}")
    userChoice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
    answer = []
    if optionA['follower_count']>optionB['follower_count']:
        answer=['A']
    elif optionA['follower_count']<optionB['follower_count']:
        answer=['B']
    else:
        answer=['A','B']

    if userChoice in answer:
        score+=1
        print(f"You're right! Current score: {score}")
        optionA = optionB
        optionB = distinctOption(optionsAmount, optionA)

    elif userChoice not in answer:
        print(f"Sorry, that's wrong. Final score: {score}")
        flag = False 

