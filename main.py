import os
import keyboard

def _clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def _options_input(options):
    selected_option = 0
    while True:
        _clear_screen()
        print("Select an option:")
        for i, option in enumerate(options):
            prefix = "* " if i == selected_option else " "
            print(f"{prefix}{option}")
        key = keyboard.read_event(suppress=True).name
        if key == 'up':
            selected_option = max(0, selected_option - 1)
        elif key == 'down':
            selected_option = min(len(options) - 1, selected_option + 1)
        elif key == 'enter':
            return selected_option
        elif key == 'x':
            exit()

def _welcome_screen():
    option = _options_input(['Use Time', 'Edit Time'])
    if option == 0:
        option = _options_input(['1', '2'])

if __name__ == "__main__":
    _welcome_screen()
