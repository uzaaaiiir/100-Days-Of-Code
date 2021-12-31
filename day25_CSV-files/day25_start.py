# with open("weather_data.csv") as file:
#     contents = file.read()
#     data = contents.split('\n')
#     data.remove(data[0])

#     for item in range(len(data)):
#         data[item] = data[item].split(sep=",")
    
#     for row in data:
#         print(row)


# CSV Library 
# import csv 

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = [] 

#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
    
#     print(temperatures)


# Using Pandas
import pandas

# Pandas assumes the first row is names of column
data = pandas.read_csv("weather_data.csv")

# Can find data using the name of column 
print(data["temp"])