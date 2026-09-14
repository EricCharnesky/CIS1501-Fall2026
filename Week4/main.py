money = float(input("How much money do you have "))
lunch = ""

if money > 15:
    lunch = 'Picasso'
elif money > 10:
    lunch = 'soup'
else:
    lunch = "ramen"

lunch = 'Picasso' if money > 15 else "soup" if money > 10 else "ramen"


#if 10 * 20 > 15 - 5:

color = input("Enter your favorite color: ")

if color > "RED":
    print("Greater than red?!?")
else:
    print("Less than red?!?!")


items_to_sell = {
    "strawberries" : 5,
    "pineapples" : 6,
    "mangoes" : 4
}

item_to_buy = input("Enter an item to buy: ")


if item_to_buy not in items_to_sell:
    print("We don't sell that, try again")
    item_to_buy = input("Enter an item to buy: ")

# looks for matching keys
if item_to_buy in items_to_sell:
    quantity = int(input("How many? "))
    print(quantity * items_to_sell[item_to_buy])
else:
    print("We don't sell that")

word_to_guess = "xylophone"

guess = input("Enter a letter to guess: ")

if len(guess) > 1:
    print("No cheating!")

    # do better next week
    exit()

if guess in word_to_guess:
    print("You got a letter!")


classes = ['CIS 2001', 'PHYS 150', 'MAT 451', 'STAT 305']

class_for_winter = input("Enter a class to take this winter: ")

if class_for_winter in classes:
    print("Great, that's on your list!")
else:
    print("Are you sure you want to take that?")


number = int(input("Enter a number: "))
remainder = number % 2

if remainder == 1:
    print("You picked an odd number")
else:
    print("You picked an even number")

# with numbers, anything other than 0 is true
if number % 2:
    print("You picked an odd number")
else:
    print("You picked an even number")


monthly_salary = int(input("Enter your monthly salary: "))
age = int(input("Enter your age: "))

if ( monthly_salary > 3000 and age > 30 ) or monthly_salary > 5000:
    print("You can get a loan")
else:
    print("No loan for you")

# true and true == true
# true and false == false
# false and true == false
# false and false == false

# true or true == true
# true or false == true
# false or true == true
# false or false == false



score = float(input("Enter your score for test 1: "))

if score > 93:
    print("A")
elif score > 90:
    print("A-")
elif score > 87:
    print("B+")
else:
    print("F")


if score > 93:
    print("A")
if 93 >= score > 90:
    print("A-")
if 90 >= score > 87:
    print("B+")
else:
    print("F")

if score > 93:
    print("A")
if 93 >= score and score > 90:
    print("A-")
if 90 >= score and score > 87:
    print("B+")
else:
    print("F")






money_in_my_pocket = float(input("How much money is in your pocket? "))

if money_in_my_pocket > 15.00:
    print("Go to picasso")
    choice = input("What do you want, tacos or pizza?").lower()
    if choice == 'pizza':
        print("pizza is $12.50")
    elif choice == "tacos":
        print("tacos are $13.49")
    else:
        print(f"we don't serve {choice}")
else:
    print("You get ramen")



name = input("Enter your name: ")

if name != "Eric":
    print("Don't forget to do your homework")
else:
    print("Hi there lecturer")


if name == "Eric":
    print("Hi there lecturer")
else:
    print("Don't forget to do your homework")


