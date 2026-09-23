import random


total = 0
receipt = float(input("Enter a receipt value to total or 0 to stop: "))
while receipt != 0:
    total += receipt
    receipt = float(input("Enter a receipt value to total or 0 to stop: "))
else:
    print(f"Total ${total}")

total = 0
receipt = float(input("Enter a receipt value to total or 0 to stop: "))
while True:
    total += receipt
    receipt = float(input("Enter a receipt value to total or 0 to stop: "))
    if receipt == 0:
        break
else: # won't run if you use break
    print(f"Total ${total}")



size = int(input("What size square?"))

for row in range(size):
    print("*" * size)


length = int(input("enter the length: "))
height = int(input("Enter the height: "))

for row in range(height):
    print("*" * length)

height = int(input("Enter the height of your right angle triangle: "))

for length in range(1,height+1):
    print("*" * length)

for length in range(1,height+1):
    print(f'{" " * (height - length)}{"*" * length}')


base = 0
while base % 2 != 1: # while the remainder isn't 1
    base = int(input("Enter an odd number base for an equilateral triangle"))


spaces = base // 2
stars = 1

while stars <= base:
    print(f"{" "*spaces}{"*"*stars}")
    stars += 2
    spaces -= 1

# undoing the last change
stars -= 2
spaces += 1

while stars >= 1:
    stars -= 2
    spaces += 1
    print(f"{" " * spaces}{"*" * stars}")




number_of_samples = int(input("Enter the number of times to roll: "))
sides_on_die = int(input("how many sides are on your die? "))
how_many_rolls_to_sum = int(input("How many times are you rolling to sum: "))

roll_count = [ 0 ] * (sides_on_die * how_many_rolls_to_sum + 1)

for roll in range(number_of_samples):
    total = 0
    for roll_to_sum in range(how_many_rolls_to_sum):
        total += random.randint(1,sides_on_die)
    roll_count[total] += 1

for index in range(how_many_rolls_to_sum,len(roll_count)):
    percentage = int(roll_count[index] / number_of_samples * 100)
    print(f'{index:02d}: {'*' * percentage}')

for index, value in enumerate(roll_count):
    if index < how_many_rolls_to_sum:
        continue
    percentage = int(value / number_of_samples * 100)
    print(f'{index:02d}: {'*' * percentage}')


print(roll_count)



keyword = "STOP"

command = input("Enter a command")

while True:
    print(command)
    command = input("Enter a command")
    if command == keyword:
        break # immediate exit of the loop
    print("more loop running")


for number in range(100):
    if number % 2:
        continue # jump back to the loop condition
    # else: - else is redundant
    print(number)


for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(f'{hour:02d}:{minute:02d}:{second:02d}')

for number in range(2, 50, 2):
    print(number)

for number in range(100, 50, -1):
    print(number)

foods = ['tacos', 'cheeseburger', 'pizza']

for index in range(len(foods)):
    print(foods[index])


name = input("Enter your name: ")

for letter in name:
    print(chr(ord(letter)+1), end="")
print()

index = 0
while index < len(name):
    print(name[index])
    index += 1

number = 10

while number > 0:
    print(number)
    number -= 1

choices = ["rock", "paper", "scissors"]

index = 0
while index < len(choices):
    choices[index] = choices[index].upper()
    index += 1

# can't change items in collections with a for loop
for choice in choices:
    choice = choice.lower()

choice = ""

# validation loop with strings
while choice not in choices:
    choice = input("Enter rock paper or scissors: ").upper()

score = -1

# validation loop with numbers
while not (0 < score <= 100):
    score = int(input("Enter your score 0-100: "))

# for every item in the collection - iterates
for choice in choices:
    print(choice)




print("Blast off!!")