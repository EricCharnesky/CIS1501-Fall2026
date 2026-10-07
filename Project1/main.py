import random

def get_option_from_list_lower_case(list):
    choice = ""
    while choice not in list:
        choice = input(f"Pick an item from the list: {list}").lower()
    return choice

def get_random_value_negative_10_to_positive_10():
    value = random.randint(-10, 10)
    return value

def self_destruct(current_distance):
    cancelation_code = ""
    while current_distance != 1 and cancelation_code != "CANCEL":
        cancelation_code = input("Self destruct active, please enter cancelation code: ")
        current_distance -= 1
    return current_distance, cancelation_code == "CANCEL"

def check_for_crash(tilt):
    # 0 is false, everyting else is true
    return tilt

def get_closer_to_surface_and_check_for_crash(current_distance, x_tilt, y_tilt):
    current_distance -= 1

    if current_distance == 0 and \
        ( check_for_crash(x_tilt) or check_for_crash(y_tilt) ):
        print("CRASH")

    return current_distance

yes_or_no_choices = ('yes', 'no')
valid_commands = ("thrusters", "self destruct", 'x+', 'x-', 'y+', 'y-', 'nothing')

while get_option_from_list_lower_case(yes_or_no_choices) == 'yes':
    x_tilt = get_random_value_negative_10_to_positive_10()
    y_tilt = get_random_value_negative_10_to_positive_10()

    current_distance = 10

    is_self_destruct_mode_active = False

    while current_distance > 0:
        print(f'Distance: {current_distance} - X tilt: {x_tilt} - Y tilt {y_tilt} ')
        command = get_option_from_list_lower_case(valid_commands)

        if command == "self destruct":
            current_distance, cancelled = self_destruct(current_distance)
            is_self_destruct_mode_active = not cancelled
        elif command == "x-":
            x_tilt -= 1
        elif command == "x+":
            x_tilt += 1
        elif command == "y-":
            y_tilt -= 1
        elif command == "y+":
            y_tilt += 1
        elif command == "thrusters":
            current_distance += 2

        current_distance = get_closer_to_surface_and_check_for_crash(current_distance, x_tilt, y_tilt)

    if x_tilt == 0 and y_tilt == 0 and not is_self_destruct_mode_active:
        print("successfully landed!")
