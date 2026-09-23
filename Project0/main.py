import math

valid_items = ('pizza', 'salad', 'pop')

total_guests = int(input("How many guests are you inviting?")) + 1

item_to_serve = input("Are you serving, pizza, salad, or pop?")
while item_to_serve not in valid_items:
    print("invalid item, try again!")
    item_to_serve = input("Are you serving, pizza, salad, or pop?")

item_cost = float(input(f"How much does it cost per {item_to_serve}"))

if item_to_serve == 'pizza':
    items_per_person_factor = 1/3
elif item_to_serve == 'salad':
    items_per_person_factor = 1 / 4
else:
    items_per_person_factor = .75 / 2

items_to_buy = math.ceil(total_guests * items_per_person_factor)

print(f"You need to buy {items_to_buy} {item_to_serve}, expected cost is: ${items_to_buy*item_cost:.2f}")
