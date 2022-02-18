#목표1. 3가지 색상의 다람쥐
#목표2. 각 색상별로 다람쥐가 몇 마리나 있는지_Primary Fur Color
#목표3. squirrels_count.csv 만들기


import pandas

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")

color = squirrels["Primary Fur Color"]
ls_color = color.tolist()

gray_color = ls_color.count("Gray")
cinnamon_color = ls_color.count("Cinnamon")
black_color = ls_color.count("Black")

squirrels_dic = {
    "Fur color": ["gray", "red", "black"],
    "Count": [gray_color, cinnamon_color, black_color],
                 }

result = pandas.DataFrame(squirrels_dic)
result.to_csv("new_squirrels_data.csv")

