def citation_generator(name, author, publisher, year_published):
    print(f'{name}, {author} {publisher}. ({year_published})')

# assigning a default value
def print_date(day, month, year=2026):
    print(f'{year}-{month}-{day}')

# don't create lists as defaults
def get_list(prompt, some_list=None):
    if some_list is None:
        some_list = []
    choice = input(prompt)
    some_list.append(choice)
    return some_list


def get_option_from_list(list):
    choice = ""
    number_of_tries = 0
    while choice not in list:
        choice = input(f"Pick an item from the list: {list}")
        number_of_tries += 1
    return choice, number_of_tries


def change_number(number):
    number += 1
    print(number)

"""
some notes about this

more notes
"""
def upper_case_list(some_list):
    for index in range(len(some_list)):
        some_list[index] = some_list[index].upper()
        print(some_list[index])
    some_list.clear()
    some_list.append('tofu')


print_date(9, 30)

print_date(1,1, 2000)

# comma separate to 'unpack' the multiple values returned
choice, attempts = get_option_from_list(('yes', 'no'))
print(choice)


number = 10
change_number(number)
change_number(number)
change_number(number)
print(number)

foods = ['burger', 'tacos', 'steak']

for index, item in enumerate(foods):
    print(f'{index}: {item}')

print(foods)
# some_list[:] returns a copy of the list
upper_case_list(foods[:])
print(foods)

for number in range(0, 10, 2):
    print(number)
# positional arguments
citation_generator( "Odyssey","Homer", "self published", "8th century BC")

citation_generator(author="Homer", name="Odyssey", publisher="self published", year_published="8th century BC")