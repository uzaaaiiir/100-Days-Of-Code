def calculatorArt():
    logo = """
    _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """
    print(logo)

def calculation(n1, n2, operation):
    '''(number, number, str)->number
    Function takes two number and an operation(string: + - / *).
    Returns the result of the operation
    Precondition: The operation is + - / *, represented as a string 
    '''
    if operation=='/':
        return n1/n2
    elif operation=='*':
        return n1*n2
    elif operation=='+':
        return n1+n2
    elif operation=='-':
        return n1-n2

def beginCalc():
    firstNumber = getInput()
    operation = getOperation()
    secondNumber = getInput_v2()
    result = calculation(firstNumber, secondNumber, operation)
    print(f"{firstNumber} {operation} {secondNumber} = {result}")
    return result 

def getInput():
    '''(None)->number
    Function prompts the user for a number and returns it.
    '''
    flag = True 
    while flag:
        try:
            firstNumber = float(input("What's the first number?: "))
            flag = False
        except:
            print("Please enter a number.")
    return firstNumber

def getInput_v2():
    '''(None)-> number
    Function prompts the user for a number and returns it.
    '''
    flag = True 
    while flag:
        try:
            secondNumber = float(input("What's the next number?: "))
            flag = False
        except:
            print("Please enter a number.")
    return secondNumber

def getOperation():
    '''(None)->str
    Function prompts the user for an operation from '+', '-', '/' and '*' and returns it. 
    '''
    flag = True
    while flag:
        operation=input("+\n-\n*\n/\nPick an operation: ")
        if operation in ['/','*','+','-']:
            flag = False
        else:
            print("Please enter a correct operation.")
    return operation

# main
calculatorArt()

result = beginCalc()

flag = True 
while flag:
    continueCalc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower().strip()
    if continueCalc == 'y':
        firstNumber = result
        operation = getOperation()
        secondNumber = getInput_v2()
        result = calculation(firstNumber, secondNumber, operation)
        print(f"{firstNumber} {operation} {secondNumber} = {result}")
    elif continueCalc=='n':
        print("\033c")
        calculatorArt()
        result = beginCalc()
    else:
        print("Please enter 'y' or 'n'.") 