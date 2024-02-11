#содержит классы и функции для работы с датами и временем в Python.
import datetime 
x = datetime.datetime.now()
print(x)
# он выводит текущую дату и время 
# The date contains year, month, day, hour, minute, second, and microsecond.


import datetime 
x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
import datetime 
x = datetime.datetime(2005 , 9 , 19)
print(x)

