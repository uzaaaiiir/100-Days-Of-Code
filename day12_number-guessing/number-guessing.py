import random

def guess_art():
    art = '''
    .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |    ______    | || | _____  _____ | || |  _________   | || |    _______   | || |    _______   | |
    | |  .' ___  |   | || ||_   _||_   _|| || | |_   ___  |  | || |   /  ___  |  | || |   /  ___  |  | |
    | | / .'   \_|   | || |  | |    | |  | || |   | |_  \_|  | || |  |  (__ \_|  | || |  |  (__ \_|  | |
    | | | |    ____  | || |  | '    ' |  | || |   |  _|  _   | || |   '.___`-.   | || |   '.___`-.   | |
    | | \ `.___]  _| | || |   \ `--' /   | || |  _| |___/ |  | || |  |`\____) |  | || |  |`\____) |  | |
    | |  `._____.'   | || |    `.__.'    | || | |_________|  | || |  |_______.'  | || |  |_______.'  | |
    | |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
    '''
    print(art)

def guess_number(number, lives):
    user=0
    while user!=number and lives!=0:
        print(f"You have {lives} attempts remaining to guess the number.")
        flag = True
        while flag: 
            try:
                user = int(input("Make a guess: "))
                if user<0:
                    print("Please enter a positive integer between 1 and 100.")
                else:
                    flag = False
            except: 
                print("Please enter an integer.")
        if user > number and lives!=1:
            print("Too high.\nGuess again.")
            lives = lives - 1
        elif user < number and lives!=1:
            print("Too low.\nGuess again.")
            lives = lives -1 
        elif user != number and lives==1:
            if user < number:
                print("Too low.")
            elif user > number:
                print("Too high.")
            print("You've run out of guesses, you lose.")
            lives = lives-1
        else: 
            print(f"You got it! The answer was {number}")
        
guess_art()
print("Welcome to the Number Guessing Game!")
number = random.randint(0,100)
print("I Am thinking of a number between 1 and 100.")
print(f"Psst, the correct answer is {number}")

EASY = 10
HARD = 5

flag = True
while flag:
    user = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    if user == 'easy':
        guess_number(number, EASY)
        flag=False
    elif user=='hard':
        guess_number(number, HARD)
        flag=False
    else:
        print("Please enter a correct input.")

