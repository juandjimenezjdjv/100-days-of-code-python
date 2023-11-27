
# file=open("weather_data.csv", "r")
# data=file.readlines()
# #lista=data.split("\n")
# file.close()
# print(file)
# print(lista)

import csv

# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data=pandas.read_csv("weather_data.csv")
#print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(data[data.temp == data["temp"].max()])

#Creat a data frame from scratch
# data_dict= {
#     "students": ["Ammy", "James", "Angela"],
#     "scores": [76, 56, 64]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print (data)
data=pandas.read_csv("centralsquirrel.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel count.csv")