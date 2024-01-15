import pickle
from classes import Time
import time
import win32gui
import win32con
from win32api import GetSystemMetrics

data_file_path = "C:/Users/Lim Wei Jen/Documents/Coding Projects/no-screen-time/data.pkl"

hwnd = win32gui.GetForegroundWindow()

# Dictionary to store time used for each category
time_used = {}

# Function to bring the window to the front
def focus_window():
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, GetSystemMetrics(0), GetSystemMetrics(1), 0)

# Function to move the window to the background
def defocus_window():
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, GetSystemMetrics(0)//4, GetSystemMetrics(1)//4, 0)

# Function to retrieve times from a pickle file
def get_times():
    with open(data_file_path, 'rb') as file: return pickle.load(file)

# Initiates a countdown timer, bringing the window to the background during the countdown
def start_timer(t):
    defocus_window()
    for remaining_time in range(int(t) * 60, 0, -1):
        minutes, seconds = divmod(remaining_time, 60)
        print(f"Time left: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(1)

# Called after the timer ends, updating the time used for a specific category while bringing the window to the foreground
def end_timer(time_name, time_used_for_the_specific_time):
    if time_name in time_used:
        time_used[time_name] += int(time_used_for_the_specific_time)
    else:
        time_used[time_name] = int(time_used_for_the_specific_time)
    focus_window()

# Gets the allocated time for a specific category
def get_time_allocated(time_name, originalTime=True):
    for t in get_times():
        if t.name == time_name:
            if t.name in time_used and not originalTime:
                return int(t.time) - int(time_used[t.name])
            return t.time

# Edit the allocated time for the specific category
def edit_time(time_name, new_time):
    times = []
    for t in get_times():
        if t.name == time_name:
            t.time = new_time
        times.append(t)
    with open(data_file_path, 'wb') as file:
        pickle.dump(times, file)

# Create a new time category
def new_time(time_name, new_time):
    times = get_times()
    times.append(Time(time_name, new_time))
    with open(data_file_path, 'wb') as file:
        pickle.dump(times, file)

# Delete an existing time category
def delete_time(time_name):
    new_times = []
    for t in get_times():
        if t.name != time_name:
            new_times.append(t)
    with open(data_file_path, 'wb') as file:
        pickle.dump(new_times, file)
