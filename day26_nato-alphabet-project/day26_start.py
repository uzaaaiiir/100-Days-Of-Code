import random 

# List comprehension
# Adds 1 to each number 
numbers = [1, 2, 3]
numbers_new = [n + 1 for n in numbers]
print(numbers_new)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Creating new list with each number squared 
numbers_squared = [num**2 for num in numbers]
# Creating new list only of the even numbers 
even_numbers = [num for num in numbers if num % 2 == 0]


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# List using strings 
cap_names = [name.upper() for name in names if len(name) > 5]
# Creating dictionary from a list 
name_scores = {name:random.randint(1,100) for name in names}
passed_students = {name:score for (name,score) in name_scores.items() if score >=50}