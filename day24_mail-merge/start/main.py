# Opening, reading, closing file 
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Opening, reading, closing file using 'with' keyword
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Writing to file 
with open("my_file.txt", 'w') as file:
    # Will delete all previous content of file 
    file.write("New text.")

# If file does not exist, creates a new file 
with open("new_file.txt", mode="w") as file:
    file.write("New Text.")