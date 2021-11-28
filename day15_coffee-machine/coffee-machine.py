
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def printReport(resources):
    '''(dict)->None
    Function prints the resources left in the coffee machine and the money in the coffee machine.
    '''
    print(f'Water: {resources["water"]}mL')
    print(f'Milk: {resources["milk"]}mL')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')

def getInput():
    '''(None)->str
    Function prompts the user for a choice.
    Checks if the input is correct option, returns the choice.
    '''
    correct_Input = True
    while correct_Input:
        userChoice = input("What would you like? (Espresso/Latte/Cappuccino): ").strip().lower()
        if userChoice in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
            correct_Input = False
    return userChoice

def checkResources(userDrink, resources, MENU):
    '''(dict, str, dict of dicts)->str
    Function takes as input a dict of the available resources in the machine, a str representing the drink chosen,
    and a dict of dicts representing the drinks and resources, costs.
    Function returns if there is insufficient resources.
    '''
    drinkResources = MENU[userDrink]["ingredients"]
    for ingredient in drinkResources:
        if resources[ingredient] - drinkResources[ingredient] < 0:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def processCoins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    amountGiven = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return amountGiven

def updateResources(userChoice, MENU, resources):
    drinkResources = MENU[userChoice]["ingredients"]
    for ingredient in drinkResources:
        resources[ingredient] = resources[ingredient] - drinkResources[ingredient]
    resources["money"] = resources["money"] + MENU[userChoice]["cost"]
    return resources

# TODO: Prompt user for what they would like 
machine_Status = True
while machine_Status:
    userChoice = getInput()
    if userChoice == 'report':
        printReport(resources)
    elif userChoice in ['latte', 'espresso', 'cappuccino']:
        if checkResources(userChoice, resources, MENU):
            coinsGiven = processCoins()
            if coinsGiven >= MENU[userChoice]["cost"]:
                print(f'Here is ${round((coinsGiven - MENU[userChoice]["cost"]),2)} in change.')
                print(f'Here is your {userChoice} ☕. Enjoy!')
                resources = updateResources(userChoice, MENU, resources)
            else:
                print("Sorry, that's not enough money. Money refunded.")
    elif userChoice == 'off':
        machine_Status = False 

    



