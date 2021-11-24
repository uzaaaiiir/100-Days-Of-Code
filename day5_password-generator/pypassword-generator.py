import random

def ascii_name_plaque(name):
     '''(str)->None
     Takes a string as an input, prints out a name plaque
     Preconditions: name is a string, any quotes in the name must be single quotes
     '''
     length = len(name)
     print(5*"*" + length*('*') + 5*"*")
     print("*" + 4*" " + length*" " + 4*" " + "*")
     print("*" + "  "+ "__" + name + "__" + "  " + "*")
     print("*" + 4*" " + length*" " + 4*" " + "*")
     print(5*"*" + length*('*') + 5*"*")

def randomPassword(inputLetters, inputNumbers, inputSymbols):
    '''(int, int, int)->list of str
    Takes three integers representing how many numbers, letters, and symbols the user wants in the password.
    Returns a list of randomly generated elements with a certain number of numbers, letters, and symbols.
    Preconditions: inputLetters, inputNumbers, and inputSymbols are integers
    '''
    letters = [
        'a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
        'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

    lettersRandom = random.choices(letters, k=inputLetters)
    numbersRandom = random.choices(numbers, k=inputNumbers)
    symbolsRandom = random.choices(symbols, k=inputSymbols)

    password = (lettersRandom + numbersRandom + symbolsRandom)
    return password

def passwordFinal(password):
    '''(list of str)->str
    Takes a list of strings and returns a string with all the items concatenated into a single string.
    Preconditions: password is a list of strings
    '''
    finalPassword = ''
    for item in password:
        finalPassword = finalPassword + item
    return finalPassword

#main 
ascii_name_plaque("Welcome to the Python Password Generator")
inputLetters = int(input("How many letters would you like in your password?\n"))
inputNumbers = int(input("How many numbers would you like in your password?\n"))
inputSymbols = int(input("How many symbols would you like in your password?\n"))

password = randomPassword(inputLetters, inputNumbers, inputSymbols)
random.shuffle(password)

print(f"Here is your password: {passwordFinal(password)}")

