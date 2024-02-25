# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
txt = input(str())
x = re.findall( r"a.*b\b"  , txt)
print(x)