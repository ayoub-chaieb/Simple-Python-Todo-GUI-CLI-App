import csv

with open("weather.csv", "r") as weather:
    data = list(csv.reader(weather))

city = input("ENter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])
