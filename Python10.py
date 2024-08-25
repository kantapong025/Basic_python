"""
#
Part: Python JSON
# API = Application Programming Interface
#
"""
import json

# make a json (String)
x = '{"name": "John", "age": 20, "city": "Phuket"}'
print(x)

# parse
y = json.loads(x)

# python dictionary
print(y)
print(type(y))
print(y["city"])

# python dictionary
a = {
    "name": "Noah",
    "age": 20,
    "city": "Phuket"
}

# convert to JSON(String)
b = json.dumps(a)

# JSON String
print(b)