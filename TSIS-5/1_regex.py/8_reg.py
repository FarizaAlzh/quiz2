# Write a Python program to split a string at uppercase letters.
import re
txt = input(str())
x = re.findall('[A-Z][a-z]*' , txt)
print(x)