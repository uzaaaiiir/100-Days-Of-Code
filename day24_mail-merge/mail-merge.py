PLACEHOLDER = "[name]"

# Read names you want to write emails to
with open("./Input/Names/invited_names.txt") as invited_names:
    invited_names = invited_names.read()
    invited_names = invited_names.split('\n')
    print(invited_names)

# Writes letter and stores in folder
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    starting_letter = starting_letter.read()

    # Creates letters
    for name in invited_names: 
        file = open(f"Output/ReadyToSend/letter_for_{name}.txt", mode='w')
        file.write(starting_letter.replace(PLACEHOLDER, name)) 