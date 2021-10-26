import random

def rps_num(option):
    if option == 'rock':
        return 0
    elif option == 'paper':
        return 1
    elif option == 'scissors':
        return 2

def rps_image(n):
    if n==0:
        print("     _______")
        print("---'    ____)")
        print("     (_____)")
        print("     (_____)")
        print("     (____)")
        print("---.__(___)")
    elif n==1:
        print("     _______")
        print("---'    ____)____")
        print("           ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)")
    elif n==2:
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")

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

def rps():
    player1 = rps_num(input("What do you choose? Enter Rock, Paper, or Scissors:\n").strip().lower())
    rps_image(player1)
    print("\n")

    print("Computer chose:", end=" ")
    player2 = random.randint(0,2)
    if player2==0:
        print("Rock")
    elif player2==1:
        print("Paper")
    else:
        print("Scissors")

    rps_image(player2)
    print("\n")

    if player1==player2:
        print("Tie.")
    elif (player1==0 and player2==2) or (player1==1 and player2==0) or (player1==2 and player2==1):
        print("You win!")
    else:
        print("You lose.\u2639")
