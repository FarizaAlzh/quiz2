# Write a Python program to print yesterday, today, tomorrow.
import datetime 
today = datetime.datetime.now().date()
yesterday = today - datetime.timedelta(1)
tomorrow = today + datetime.timedelta(1)
print(yesterday)
print(today)
print(tomorrow)