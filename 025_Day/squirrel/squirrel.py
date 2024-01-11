import pandas

ABSOLUTE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/025_Day/squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240111.csv"

s_data = pandas.read_csv(ABSOLUTE_PATH)
gray_squirrels_count = len(s_data[s_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(s_data[s_data["Primary Fur Color"] == "Cinnamon"])
red_squirrels_count = len(s_data[s_data["Primary Fur Color"] == "Red"])

data_dict = {
    "Fur_Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels_count, cinnamon_squirrels_count, red_squirrels_count ]
}
Data_Frame = pandas.DataFrame(data_dict)
Data_Frame.to_csv("squirrel_count.csv")

