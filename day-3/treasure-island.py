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

name = input("What is your name? ")
ascii_name_plaque("Welcome to Treasure Island, " + name)
print("Your missions is to find the treasure.\n")

direction = input('You\'re at a cross road. Wehre do you want to go? Type "left" or "right" \n').strip().lower()

if direction=="left":
    swim = input('You\'ve come to a lake. There is an island in the middle of a lake. Type "wait" to wait for a boat. Type "swim" to swim across \n').strip().lower()
    if swim=="wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").strip().lower()
        if color=="blue":
            print("You enter a room of beats. Game Over.")
        elif color=="red":
            print("You have been burned by fire. Game Over.")
        elif color=="yellow":
            print("You found the treasure. You win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by angry trout. Game over.")
else:
    print("You fell into a hole. Game Over")


