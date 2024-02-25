# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s
import re 
txt = input(str())
x = re.findall( "a.*b" , txt)
print(x)