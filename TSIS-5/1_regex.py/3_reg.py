# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
txt = input()
x = re.findall(r'\b[a-z]+_[a-z]+',txt)
print(x)
if x :
    print("YES")
else:
    print("NO")