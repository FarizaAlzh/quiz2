# JSON - это синтаксис для хранения и обмена данными.

# Parse JSON - Convert from JSON to Python
# '{}'
import json 
x = '{"name": "Fariza" , "age": "18" , "from" : "KZ" }'
y = json.loads(x)
print(y["age"])

# Convert from Python to JSON
# {}
import json 
x = {"name": "Arai" ,
    "age":"17",
    "from" : "KZ" }
y = json.dumps(x)
print(y)


import json

print(json.dumps({"name": "John", "age": 30})) # dict 
print(json.dumps(["apple", "bananas"])) # list 
print(json.dumps(("apple", "bananas"))) # tuple
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
  "name": "Fariza",
  "age": 18,
  "married": False,
  "divorced": False,
  "children": ("Jessi","Mika"),
  "pets": True,
  "study": [
    {"place": "school num 10 named Abai" , "year" : "finish" },
    {"place": "KBTU", "year" : "1"}
  ]
}

# convert into JSON:
# y = json.dumps(x , indent =1 , separators=("! ", " -- "))
y = json.dumps(x , indent =1 , sort_keys=True)

# the result is a JSON string:
print(y)
