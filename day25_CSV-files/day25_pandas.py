import pandas 

# pandas.read_csv reads the CSV file 
data = pandas.read_csv("weather_data.csv")
""" print(type(data)) """

# Using pandas to access a column 
# print(data["temp"])
""" print(type(data["temp"])) """

# Converting data to dict
""" data_dict = data.to_dict()
print(data_dict) """

# Converting a column to a list 
""" temp_list = data["temp"]
print(temp_list.to_list()) """

# Calculating average temperature 
""" avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)
print(temp_list.mean()) """

# Max of temperatures
""" temp_max = data["temp"].max()
print(temp_max) """

# Get data in columns
# Pandas take the column headings and converts it to attributes 
""" print(data.condition) """

# Get Data from Rows in Dataframe
""" print(data[data.day == "Monday"]) """

# Can be read as go to data, and find the row where the temperature has the maximum temperature
""" print(data[data.temp == data.temp.max()]) """

# Prints a value in a row 
""" monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp * 1.8 + 32) """

# Creating data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
scores = pandas.DataFrame(data_dict)
print(scores)
scores.to_csv("scores_new.csv")
