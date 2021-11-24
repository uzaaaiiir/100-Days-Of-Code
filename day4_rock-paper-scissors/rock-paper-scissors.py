import my_module

flag = True
while flag:
    rps1 = input("Do you want to play rock, paper, scissors? Yes or No: ").strip().lower()
    if rps1=='no':
        flag=False
    elif rps1=='yes':
        my_module.rps()
    else: 
        print("Please enter Yes or No!")

my_module.ascii_name_plaque("Goodbye!")