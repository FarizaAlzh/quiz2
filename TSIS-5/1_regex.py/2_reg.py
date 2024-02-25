# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
txt = input(str())
x = re.findall( "a.{2,3}b"  , txt)
print(x)