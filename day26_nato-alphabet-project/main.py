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


# with open("nato_phonetic_alphabet.csv") as nato_alphabet:
#     nato_alphabet = [alphabet.strip("\n") for alphabet in nato_alphabet.readlines()]
#     nato_alphabet = [item.split(',') for item in nato_alphabet]
# nato_dict = {item[0]:item[1] for item in nato_alphabet}


nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
char_list = [nato_dict[char] for char in user_input]
print(char_list)
