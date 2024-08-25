"""
#
Part: Python String Formatting
# 
#
"""
price = 60
txt = f"price is {price} baht."
price(txt)
txt = f"price is {price:2f} baht."
price(txt)

price = 50
tax = 0.25
txt = f"prlce is {price + (price * tax)}"
print(txt)

price = 10000
txt = f"price is{price:,} baht."
price(txt)