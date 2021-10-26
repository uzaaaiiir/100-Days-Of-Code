print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_Bill = bill*(tip/100) + bill

per_Person = round(((total_Bill)/people),2)
print(f"Each person should pay: ${per_Person:.2f}")