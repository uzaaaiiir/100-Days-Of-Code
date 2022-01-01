import random 

# List comprehension
# Adds 1 to each number 
numbers = [1, 2, 3]
numbers_new = [n + 1 for n in numbers]

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


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence = sentence.split()
sentence_letters = {word:len(word) for word in sentence}

# Convert dictionary of temperatures in Celsius to Farhenheit
weather_c = {
    "Monday": 12, 
    "Tuesday": 14, 
    "Wednesday": 15, 
    "Thursday": 14, 
    "Friday": 21, 
    "Saturday": 22, 
    "Sunday": 24, 
}
weather_farhenheit = {day:round((temp*1.8 + 32),1) for (day, temp) in weather_c.items()}

# Iterate over Pandas dataframe
import pandas 

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# Loop through rows of dataframe
for (index,row) in student_dataframe.iterrows():
    print(row.student) 
