import pandas


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    # pass


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}


with open("nato_phonetic_alphabet.csv") as nato_alphabet:
    nato_alphabet = [alphabet.strip("\n") for alphabet in nato_alphabet.readlines()]
    nato_alphabet = [item.split(',') for item in nato_alphabet]

nato_dict = {item[0]:item[1] for item in nato_alphabet}
# print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a Word: ")
char_list = [nato_dict[char.upper()] for char in user_input]
print(char_list)
