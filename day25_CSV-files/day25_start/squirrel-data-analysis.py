import pandas 

# Reads CSV file 
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(squirrel_data)

# Gets Access of Primary Fur Color & converts to List
primary_fur_color = squirrel_data["Primary Fur Color"]
primary_fur_color = primary_fur_color.to_list()
print(primary_fur_color)

# Count the amount 
gray_count = primary_fur_color.count("Gray")
cinnamon_count = primary_fur_color.count("Cinnamon")
black_count = primary_fur_color.count("Black")

# Create dictionary
fur_color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

# Create Dataframe
fur_color_table = pandas.DataFrame(fur_color_dict)
print(fur_color_table)

# Create CSV File
fur_color_table.to_csv("squirrel_colors.csv")

