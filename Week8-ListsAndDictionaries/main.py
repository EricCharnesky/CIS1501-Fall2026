import random

def print_board(board):
    print("\n".join(str(row) for row in board))
    print()

def keep_playing():
    return input("Do you want to play tic tac toe? y/n").lower() == 'y'

def get_location_to_mark(board):
    while True:
        row_index = int(input("Enter a row index"))
        column_index = int(input("Enter a column index"))

        if row_index < 0 or row_index >= 3 or column_index < 0 or column_index >= 3:
            print("invalid index, use 0 1 or 2")
            #continue

        elif board[row_index][column_index] != ' ':
            print("spot taken")
            #continue
        else:
            return row_index, column_index

def is_game_tied(board):
    for row in board:
        if " " in row:
            return False
    return True

def has_winner_by_row(board):
    for row in board:
        if row[0] != ' ' and row[0] == row[1] and row[0] == row[2]:
            return True
    return False

def has_winner_by_diagonal(board):
    return board[1][1] != ' ' and \
            ( (board[1][1] == board[0][0] and \
            board[1][1] == board[2][2]) or \
            (board[1][1] == board[2][0] and \
            board[1][1] == board[0][2]) )

def has_winner_by_column(board):
    for column_index in range(len(board)):
        if board[0][column_index] != ' ' and \
            board[0][column_index] ==  board[1][column_index] and \
            board[0][column_index] ==  board[2][column_index]:
            return True
    return False

def game_has_winner(board):
    return has_winner_by_row(board) \
        or has_winner_by_column(board) \
        or has_winner_by_diagonal(board)

def is_game_over(board):
    return is_game_tied(board) or game_has_winner(board)

while keep_playing():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    current_player = 'X'

    while not is_game_over(board):
        print_board(board)
        print(f"{current_player}'s turn")
              
        row_index, column_index = get_location_to_mark(board)
        board[row_index][column_index] = current_player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        #current_player = 'X' if current_player == 'O' else "O"
    print_board(board)
    

board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]


row_index = int(input("Enter a row index"))
column_index = int(input("Enter a column index"))

board[row_index][column_index] = 'x'

print(board)

board_string = str(board[0]) + "\n" + str(board[1]) + "\n" + str(board[2])

loop_board_string = ""
for row in board:
    loop_board_string += str(row) + "\n"

joined_board_string = "\n".join(str(row) for row in board)

print(board_string)
print(loop_board_string)
print(joined_board_string)



numbers = []

for number in range(100):
    numbers.append(random.randint(1, 100))

print(numbers)

# can't loop over a list while removing
for number in numbers:
    if number % 2:
        numbers.remove(number)

for number in numbers[:]:
    if number % 2:
        numbers.remove(number)
        
print(numbers)


# index gives first occurance
if 81 in numbers:
    index_of_81 = numbers.index(81)
    print(f'81 is at index: {index_of_81}')
    while 81 in numbers[index_of_81+1:]:
        index_of_next_81 = numbers.index(81, index_of_81+1)
        print(f"another 81 found at {index_of_next_81}")
        index_of_81 = index_of_next_81

else:
    print('81 not in list')


some_foods = ['Taco', 'Burgers', 'Chicken']

some_foods.insert(1, "ma po tofu")

print(some_foods)

# removes by value
if 'taco' in some_foods:
    some_foods.remove("taco")
else:
    print("taco not in list")
some_foods.remove("Taco")

# defaults to last
value_removed = some_foods.pop(0)
print(value_removed)
print(some_foods)


if 7 < len(some_foods):
    some_foods.pop(7)
    del some_foods[7]

some_foods.insert(0, "fish")
some_foods.insert(0, "pasta")

print(some_foods)

# can't modify with for loop
for item in some_foods:
    item = item.title()

for index in range(len(some_foods)):
    some_foods[index] = some_foods[index].title()

for index, value in enumerate(some_foods):
    some_foods[index] = value.title()

print(some_foods)

# creates a sorted copy
sorted_listed = sorted(some_foods)

# modifies the list
some_foods.sort()

print(some_foods)