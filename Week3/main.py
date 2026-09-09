name = 'Eric'

print(len(name))

print(name.upper())


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


print(alphabet[4], alphabet[17], alphabet[8], alphabet[2])

# string concatenation - 'adds' them together
print('Your name is ' + alphabet[4] + alphabet[17] + alphabet[8] + alphabet[2])

print(f'Your name is {alphabet[4]}{alphabet[17]}{alphabet[8]}{alphabet[2]}')

# can count backwards from the end
print(alphabet[-1])

print(f'2 + 5 is {2+5}')

vehicle_miles_per_gallon = float(input("Enter your vehicles miles per gallons: "))
miles_driven_last_week = float(input("Enter how many miles you drove last week: "))
cost_per_gallon_in_dollars = float(input("Enter the cost of gas per gallon: "))

cost_for_gas_last_week = (miles_driven_last_week / vehicle_miles_per_gallon
                          * cost_per_gallon_in_dollars)

print(f"To drive {miles_driven_last_week} miles last" +
      f" week it cost about ${cost_for_gas_last_week:.2f}")


classes = ['CIS 1501', 'MAT 115', 'ASTR 123']

print(f'Your first class is {classes[0]}')

classes[0] = 'CIS 1501 CS1 for Data Scientists'

print(f'Your first class is {classes[0]}')

print(f'You are taking {len(classes)} classes this semester')

classes.append('ENG 1500')
classes.insert(1,'HHS 410')

class_to_add = input("Enter a class to add to your semester: ")
classes.append(class_to_add)

print(classes)

# if you don't give an index it will remove the last item
classes.pop(1)

print(classes)

# will crash if the item doesn't exist
classes.remove("ENG 1500")

print(classes)


# only removes the first
classes.remove("MAT 115")

print(classes)


numbers = [1, 2,3,4,5]
print(numbers)
print(f'The average number is {sum(numbers)/len(numbers)}')


# tuples are immutable 'lists'
winning_lotto_numbers = (1,2,3,4,5)
print(f'First winning number {winning_lotto_numbers[0]}')
# can't set values - winning_lotto_numbers[0] = 25

# sets are unordered and unique
stamps = { 'Eagle', 'Flag', 'Teapot' }

# key : value
gradebook = { 'Jeb' : 97, 'Vivi' : 85, 'Journey': 94, 'Jubilee': 83 }
print(gradebook)

# dictionary[key] returns the associated value - or sets the value - or add a key/value pair
print(f"Jeb's score is: {gradebook['Jeb']}")
gradebook['Jeb'] = 100
print(f"Jeb's score is: {gradebook['Jeb']}")
gradebook['Jack'] = 25

# this is weird
del gradebook['Jack']

# this more typical
gradebook.pop('Vivi')

print(gradebook)