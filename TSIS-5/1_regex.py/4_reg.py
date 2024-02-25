import re
txt = input()
x = re.findall(r'\b[a-z]+_[a-z]+',txt)
print(x)