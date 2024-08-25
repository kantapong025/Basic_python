"""
#
Part: Python Class and Object
#
"""
class MyClass:
    x = 5
    
# Call class
object1 = MyClass()
print("Object1 =",object1.x)
object2 = MyClass()
print("Object2 =",object2.x)

class SpyXFamily:
    def __init__(self, name_f, age_f):
        self.name = name_f
        self.age = age_f
    
    def __str__(self):
        # return self.name + " - " + self.age
        return f"{self.name} - {self.age}"

    def sayHi(self, last_name = "Forger"):
        print(f"Hey bruh what'sup {self.name} {last_name}")
    
p1 = SpyXFamily("Anya", 8)
print(p1.name, p1.age)
print(p1)
p1.sayHi()

p2 = SpyXFamily("Damian", 8)
print(p2.name, p2.age)
print(p2)
p2.sayHi("Desmond")



class Car:
    def __init__(self, body_color, engine_size):
        self.wheels = 4
        self.window = 4
        self.window_front = 1
        self.window_back = 1
        self.body_color = body_color
        self.engine_size = engine_size
        
def push_window_button(self):
    # do something
    pass

def pop_window_button(self):
    # do something
    pass

def calspeed(self):
    # speed = self.engine_size * 1000
    # return speed
    return self.engine_size * 1000

def turnOnFrontLight(self, status = "off"):
    if status == "on":
        # do something
        pass
    else:
        # do something
        pass
