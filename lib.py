import pickle
from classes import Time

time_used = {}

def get_times():
    with open('data.pkl', 'rb') as file: return pickle.load(file)

def use_time():
    pass

def select_time_to_use(time_name):
    pass

def start_timer(time):
    pass

def end_timer(time_name, time):
    pass

def settings():
    pass

def select_time_to_edit(time_name):
    pass

def get_time_allocated(time_name, originalTime=True):
    for t in get_times():
        if t.name == time_name:
            if time_used[t.name] and not originalTime:
                return t.time - time_used[t.name]
            return t.time

def edit_time(time_name, new_time):
    times = []
    for t in get_times():
        if t.name == time_name:
            t.time = new_time
        times.append(t)
    with open('data.pkl', 'wb') as file:
        pickle.dump(times, file)

def new_time(time_name, new_time):
    times = get_times()
    times.append(Time(time_name, new_time))
    with open('data.pkl', 'wb') as file:
        pickle.dump(times, file)

def delete_time(time_name):
    new_times = []
    for t in get_times():
        if t.name != time_name:
            new_times.append(t)
    with open('data.pkl', 'wb') as file:
        pickle.dump(new_times, file)
