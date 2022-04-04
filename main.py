from item import Item
from keyboard import Keyboard
from phone import Phone

# Inheritance
phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)
print(phone2.calculate_total_price())

print(Item.all)
print(Phone.all)

# Class methods
Item.instantiate_from_csv()
print(Item.all)

# Static methods
print(Item.is_integer(22))
print(Item.is_integer(22.0))
print(Item.is_integer(22.7))

# Code samples
keyboard = Keyboard("Keyboard", 600, 2)
keyboard.apply_discount()
print(keyboard.price)

item1 = Item("Laptop", 300, 5)
print(item1.name)
item1.name = "Other name"
print(item1.name)
total_price = item1.calculate_total_price()
print(total_price)
item1.apply_discount()
print(item1.price)
item1.send_email()

item2 = Item("Phone", 200, 50)
total_price = item2.calculate_total_price()
print(total_price)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

# Other utility classes
print(Item.__dict__)  # All attributes for class level
print(item1.__dict__)  # All attributes for instance level
