# Using with to open file 
with open("words.txt") as file:
    contents = file.readlines()
    print(contents[:20])


# Opening, reading, closing file 
file = open("words.txt")
contents = file.readlines()
print(contents[:20])
file.close()

