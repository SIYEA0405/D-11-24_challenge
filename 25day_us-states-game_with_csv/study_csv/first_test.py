# weather_day = []

# weather_condition = []
#
# with open("weather_data.csv") as weather_data:
#     weather = weather_data.readlines()
#
# for i in weather:
#     weather_day.append(i[0])
#     weather_temp.append(i[1])
#     weather_condition.append(i[2])

# import csv
# with open("weather_data.csv") as data_file:
#     weather_temp = []
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             weather_temp.append(row[1])
#     print(weather_temp)

import pandas
datas = pandas.read_csv("weather_data.csv")
# print(datas["day"]) # day의 열에 가진 값들만 가져 온다
#
# # datas_ = datas.to_dict() # 행에 있는 값들을 기준으로 열을 가져오고 dictionary로 만든다.
# # print(datas_)
#
# temps = datas["temp"].tolist()
# temps_length = len(temps)
# temps_sum = sum(temps)
# print(round(temps_sum / temps_length, 2))
# #위의 프린트 결과와 똑같다 datas["temp"].mean() mean 메서드 함수는 평균값을 구해준다
#
# print(datas["temp"].max())

# print(datas[datas.day == "Monday"])
# print(datas[datas.temp == datas.temp.max()])
# i = datas[datas.day == "Monday"]
# print(int(i.temp) * 9/5 + 32)

