# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
txt = "Sakffof ffkjdf Skof"
x = re.findall( r"\b[A-Z][a-z]*\b"  , txt)
print(x)