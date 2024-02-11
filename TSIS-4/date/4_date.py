# Write a Python program to calculate two date difference in seconds.
import datetime 
# first date 
year_1 = int(input())
month_1 = int(input())
day_1 = int(input())
# second date
year_2 = int(input())
month_2 = int(input())
day_2 = int(input())

date_1 = datetime.datetime(year_1, month_1 , day_1)
date_2 = datetime.datetime(year_2 , month_2 , day_2)
difference = (date_1 - date_2).total_seconds()
print(difference)

#total_seconds() = возвращает общее количество секунд,
