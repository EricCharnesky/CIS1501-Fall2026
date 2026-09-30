import random


number_of_dice_to_roll = int(input("Enter the number of dice to roll: "))
number_of_sides = int(input("Enter the number sides on the dice rolled: "))

results = []

for repetition in range(1_000_000):
    highest_roll = 0
    for roll in range(number_of_dice_to_roll):
        value = random.randint(1, number_of_sides)
        if value > highest_roll:
            highest_roll = value
    results.append(highest_roll)

print(f'Average total when rolling {number_of_dice_to_roll} '
      f'{number_of_sides} sided die: '
      f'{sum(results)/ len(results)}')


totals = []
for repetition in range(1000):
    lowest = 6
    total = 0
    for roll in range(4):
        value = random.randint(1,6)
        total += value
        if value < lowest:
            lowest = value
    total -= lowest
    totals.append(total)

print(f'average of rolling 4 6-sided dice and removing the lowest is {sum(totals)/len(totals)}')


totals = []
for repetition in range(1000):
    totals.append(random.randint(1, 6))
print(f"average earnings {sum(totals)/len(totals)}")