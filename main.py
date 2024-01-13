import os

from lib import delete_time, edit_time, end_timer, focus_window, get_time_allocated, get_times, new_time, start_timer

# Clear the screen base in the operating system
def _clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display options and get user input
def _options_input(options):
    _clear_screen()
    for i, option in enumerate(options):
        print(f"[{i}] {option}")
    print("(x) to return to main")
    selected_option = input("Option: ")
    if selected_option == 'x':
        _welcome_screen()
    return selected_option

def _use_specific_time_screen(time_name):
    _clear_screen()
    print("(x) to return to main")
    print(f'The total time for {time_name} left is {get_time_allocated(time_name, False)}')
    new_time = input('Decide how much time you want to use (minutes): ')
    if new_time == 'x':
        _welcome_screen()
    _clear_screen()
    start_timer(new_time)
    end_timer(time_name, new_time)
    _welcome_screen()

def _use_time_screen():
    option = _options_input([t.name for t in get_times()])
    _use_specific_time_screen(get_times()[int(option)].name)

def _edit_total_time_screen(time_name):
    _clear_screen()
    print("(x) to return to main")
    print(f'The current allocated time for {time_name} is {get_time_allocated(time_name)}')
    new_time = input('Allocate new time (minutes): ')
    if new_time != "x":
        edit_time(time_name, new_time)
    _welcome_screen()

def _edit_specific_time_screen(time_name):
    option = _options_input(["Edit Total Time", "Delete"])
    print("(x) to return to main")
    if option == 'x':
        _welcome_screen()
    elif option == "0":
        _edit_total_time_screen(time_name)
    elif option == "1":
        delete_time(time_name)
        _welcome_screen()

def _edit_time_screen():
    options = [t.name for t in get_times()]
    options.insert(0, 'Add New')
    option = _options_input(options)
    if option == 'x':
        _welcome_screen()
    elif option == "0":
        _add_new_time_screen()
    else:
        _edit_specific_time_screen(get_times()[int(option)-1].name)

def _add_new_time_screen():
    _clear_screen()
    print("(x) to return to main")
    name = input("Name for new time: ")
    if name == "x":
        _welcome_screen()
    else:
        total_time = input("Total time alocated (minutes): ")
        if total_time == "x":
            _welcome_screen()
        else:
            new_time(name, total_time)
    _welcome_screen()

def _welcome_screen():
    focus_window()
    option = _options_input(['Use Time', 'Edit Time'])
    if option == "0":
        _use_time_screen()
    elif option == "1":
        _edit_time_screen()

if __name__ == "__main__":
    _welcome_screen()
