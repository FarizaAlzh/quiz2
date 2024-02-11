# Write a Python program to drop microseconds from datetime.
import datetime
time = datetime.datetime.now()
without_microseconds = time.replace(microsecond=0)
print(without_microseconds)

# replace() и устанавливаем значение микросекунд в 0.