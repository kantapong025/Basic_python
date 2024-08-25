"""
#
# Part : Python comment
#
"""

# This is a comment
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = เวลา (s)

"""
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = เวลา (s)
"""

print ("Helloworld!!!")

"""
#
# Part : Python variables
#
"""
x = 5               # Integer
y = "Hey Bruh"      # String
print(x,y)

x = str(3)
y = int(5)
z = float(7)
print(type(x),type(y),type(z))
"""
#
# Part : Variables Names
#
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
MY_VAR = "John"
my_var2 = "John"
# 2my_var = "John"
# my-var = "John"
# my var = "John"

# Camel Case
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
my_nariable_name = "John"
"""
#
# Part : Python String
#
"""

x = "Hey Bruh"
print(x)

y = """1 Hey Bruh
2 Hey Bruh
3 Hey Bruh
"""
print(y)

x = "Hey Bruh"
print(x[2])
print(len(x))
print("Hey" in x)
print("What'sup" not in x)
print(x.upper())
print(x.lower())

print(x.replace("Bruh", "Sis"))
print(x.split(" "))

a = "Apple"
b = "Company"
print(a+" " + b)


price = 20
word = f"Price: {price:.2f}"
print(word)