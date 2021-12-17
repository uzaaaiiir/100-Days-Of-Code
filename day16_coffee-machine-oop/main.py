from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

print("\033c")
machine_Status = True 

while machine_Status:

    userChoice = input(f"What would you like? {menu.get_items()}: ").strip().lower()
    if userChoice == "off":
        machine_Status = False 
    elif userChoice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        item_in_menu = menu.find_drink(userChoice)
        if item_in_menu != None:
            enough_Resources = coffeeMaker.is_resource_sufficient(item_in_menu)
            if enough_Resources:
                enough_money = moneyMachine.make_payment(item_in_menu.cost)
                if enough_money:
                    coffeeMaker.make_coffee(item_in_menu)


