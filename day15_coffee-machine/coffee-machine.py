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
    '''(None)->float
    Function prompts the user to enter the number of coins they are giving in quarters, dimes, nickels, pennies.
    The function returns the amount based on the coins given by the user.
    '''
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    amountGiven = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return amountGiven


def updateResources(userChoice, MENU, resources):
    '''(str, dict of dicts, dict)->dict
    Function takes as input the users choice, the dict representing the menu, and a dict representing the available resources.
    Function returns the resources updated based on the choice of drink the user chose.
    Preconditions: userChoice is a valid drink in the MENU
    '''
    drinkResources = MENU[userChoice]["ingredients"]
    for ingredient in drinkResources:
        resources[ingredient] = resources[ingredient] - drinkResources[ingredient]
    resources["money"] = resources["money"] + MENU[userChoice]["cost"]
    return resources


# main

print("\033c") 
machine_Status = True
while machine_Status:
    # Gets users choice 
    userChoice = getInput()

    # Prints the report of available resources 
    if userChoice == 'report':
        printReport(resources)

    # Based on user input, gets coins from the user
    elif userChoice in ['latte', 'espresso', 'cappuccino']:

        # Checks if there's enough resources to make drink
        if checkResources(userChoice, resources, MENU):
            coinsGiven = processCoins()

            # If coins are sufficient, gives the change, and updates the resources
            if coinsGiven >= MENU[userChoice]["cost"]:
                print(f'Here is ${round((coinsGiven - MENU[userChoice]["cost"]),2)} in change.')
                print(f'Here is your {userChoice} ☕. Enjoy!')
                resources = updateResources(userChoice, MENU, resources)

            # If coins are insufficient, refunds the user
            else:
                print("Sorry, that's not enough money. Money refunded.")
    
    # Turns off the coffee machine 
    elif userChoice == 'off':
        machine_Status = False 

    



