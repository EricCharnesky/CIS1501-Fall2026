

def get_option_from_list_lower_case(list):
    choice = ""
    while choice not in list:
        choice = input(f"Pick an item from the list: {list}").lower()
    return choice

def get_random_value_negative_10_to_positive_10():
    # FIXME
    return 0

def self_destruct():
    pass

def check_for_crash(tilt):
    # FIXME
    return True

def get_closer_to_surface_and_check_for_crash(current_distance, x_tilt, y_tilt):
    # FIXME
    if check_for_crash(x_tilt) or check_for_crash(y_tilt):
        print("CRASH")

    return current_distance

yes_or_no_choices = ('yes', 'no')
valid_commands = ("thrusters", "self destruct", 'x tilt +')

while get_option_from_list_lower_case(yes_or_no_choices) == 'yes':
    x_tilt = get_random_value_negative_10_to_positive_10()
    y_tilt = get_random_value_negative_10_to_positive_10()

    current_distance = 10

    is_self_destruct_mode_active = False

    command = get_option_from_list_lower_case(valid_commands)

    if command == "self destruct":
        self_destruct()
        is_self_destruct_mode_active = True

    current_distance = get_closer_to_surface_and_check_for_crash(current_distance, x_tilt, y_tilt)


