# Write a Python program to subtract five days from current date.
import datetime

date_now = datetime.datetime.now().date()
date_5days_ago = date_now - datetime.timedelta(days=5)
print(date_now)
print(date_5days_ago)

# timedelta(days=5) представляет разницу между двумя моментами времени. 
