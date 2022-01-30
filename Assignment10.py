"""Assignment Ten: Print Summary Statistics
    Submitted by Shreya Raj
    Submitted:  June 20, 2020
    This program implements the remaining menu options:
    get_avg_temperature_day_time(), get_summary_statistics(),
    print_summary_statistics(), and choose_units() and convert_units().
"""

import math

units = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
}


def convert_units(celsius_value, unit):
    if unit == 0:
        return celsius_value
    if unit == 1:
        return celsius_value * 1.8 + 32
    if unit == 2:
        return celsius_value + 273.15


def test_sensor_setup(sensor_list, active_sensors):
    print("Testing sensor_list length:")
    if len(sensor_list) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing sensor_list content:")
    rooms_list = [i[0] for i in sensor_list]
    descriptions_list = [i[1] for i in sensor_list]
    if "4213" not in rooms_list or "Out" not in rooms_list:
        print("Fail - something is wrong with the room numbers")
    elif "Foundations Lab" not in descriptions_list:
        print("Fail - something is wrong with room descriptions")
    else:
        print("Pass")

    print("Testing active_sensors length:")
    if len(active_sensors) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing active_sensors content:")
    if sum(active_sensors) == 20:
        print("Pass\n")
    else:
        print("Fail")


def print_header():
    """Print a header."""
    print("STEM Center Temperature Project")
    print("Shreya Raj\n")


def print_menu():
    """prints menu for user to select the function that they would like to call"""
    print("Main Menu")
    print("---------")
    print("1 - Process a new data file")
    print("2 - Choose units")
    print("3 - Edit room filter")
    print("4 - Show summary statistics")
    print("5 - Show temperature by date and time")
    print("6 - Show histogram of temperatures")
    print("7 - Quit\n")


def new_file(dataset):
    print("Please enter the filename of the new data set:")
    process_file_response = dataset.process_file(input())
    if process_file_response:
        number_of_samples = dataset.get_loaded_temps()
        print('Loaded', number_of_samples, 'samples.')
        while dataset._name_of_data_set == "Unnamed":
            print('Please provide a 3 to 20 character name for the data set:')
            client_name = input()
            dataset.name = client_name
    else:
        print('Unable to load the file')


current_unit = 0  # default value indicates units in celsius


def choose_units():
    global current_unit

    print("Current units in", units[current_unit][0], "\n")
    while True:
        print("Choose your preferred units:")
        for number, unit in units.items():
            print(number, ":", unit[0])  # menu

        print("Which unit do you choose?")
        try:
            user_unit = int(input())  # the key in the key value pair
            if user_unit in units:
                current_unit = user_unit
                return  # this sets the new unit to the one chosen by the user
            print("Please choose a unit from the list")  # if it isn't an option

        except ValueError:
            print("***Please enter a number only***")


def change_filter(sensor_list, active_sensors):
    sensors = {}
    for i in sensor_list:
        sensors.update({i[0]: i[2]})

    while True:
        print(" ")
        print_filter(sensor_list, active_sensors)
        print(" ")
        print('Type the sensor to toggle (e.g. 4201) or x to end: ')
        key = input()

        if key in sensors and sensors[key] in active_sensors:
            active_sensors.remove((sensors[key]))
            continue
        elif key in sensors:
            active_sensors.append((sensors[key]))
            continue
        elif key == "x":
            break
        else:
            print("Invalid Sensor")
            print(" ")
            continue


def print_summary_statistics(dataset, active_sensors):
    summary_statistics = dataset.get_summary_statistics(active_sensors)
    if summary_statistics is None:
        print("Please load data file and make sure at least one sensor is active")
        return
    print("Summary statistics for", dataset.name, "\n")  # "Test week" in the example
    print("Minimum Temperature:",
          convert_units(summary_statistics[0], current_unit),
          # passes "minimum temperature" from get_summary_stats and current unit
          # into convert units which returns the temperature in the specified unit
          units[current_unit][1])  # this adds the C, F, or K to the end
    print("Maximum Temperature:",
          convert_units(summary_statistics[1], current_unit),
          units[current_unit][1])
    print("Average Temperature:",
          convert_units(summary_statistics[2], current_unit),
          units[current_unit][1])


def print_temp_by_day_time(dataset, active_sensors):
    print("Print Temp by Day/Time Function Called\n")


def print_histogram(dataset, active_sensors):
    print("Print Histogram Function Called\n")


'''our lists'''

sensor_list = [("4213", "STEM Center", 0),
               ("4201", "Foundations Lab", 1),
               ("4204", "CS Lab", 2),
               ("4218", "Workshop Room", 3),
               ("4205", "Tiled Room", 4),
               ("Out", "Outside", 10)]

active_sensors = [sensor_list[0][2],
                  sensor_list[1][2],
                  sensor_list[2][2],
                  sensor_list[3][2],
                  sensor_list[4][2],
                  sensor_list[5][2]]

'''function which recursively sorts the sensor list (for option 3)'''


def swap(new_list, pos0, pos1):
    temp = new_list[pos0]
    new_list[pos0] = new_list[pos1]
    new_list[pos1] = temp


def recursive_sort(list_to_sort, key=0):
    if key == 0:
        new_list = list(list_to_sort)
        swap_count = 0

        for i in range(0, len(new_list) - 1):
            if new_list[i] > new_list[i + 1]:
                swap(new_list, i, i + 1)
                swap_count = swap_count + 1
            elif new_list[i] <= new_list[i + 1]:
                continue

        if swap_count > 0:
            return recursive_sort(new_list, key)

        if swap_count == 0:
            return new_list
    elif key == 1:
        new_list = list(list_to_sort)
        swap_count = 0

        for i in range(0, len(new_list) - 1):
            if new_list[i][1] > new_list[i + 1][1]:
                swap(new_list, i, i + 1)
                swap_count = swap_count + 1
            elif new_list[i][1] <= new_list[i + 1][1]:
                continue

        if swap_count > 0:
            return recursive_sort(new_list, key)

        if swap_count == 0:
            return new_list
    else:
        print('ValueError')


'''this function marks each sensor as active or not active'''


def print_filter(sensor_list, active_sensors):
    sorted_list = recursive_sort(sensor_list, 0)
    for i in sorted_list:
        if i[2] in active_sensors:
            print(i[0], ":", i[1], " ", "[ACTIVE]")
        else:
            print(i[0], ":", i[1])


'''the class from assignment 8'''


class TempDataset:
    total_num_objects = 0

    def __init__(self):
        self._name_of_data_set = "Unnamed"
        self._data_set = []
        TempDataset.total_num_objects += 1

    @classmethod
    def get_num_objects(cls):
        return TempDataset.total_num_objects

    @property
    def name(self):
        return self._name_of_data_set

    @name.setter
    def name(self, new_name):
        if len(new_name) < 3:
            return ValueError
        elif len(new_name) > 20:
            return ValueError
        else:
            self._name_of_data_set = new_name

    def process_file(self, filename):
        try:
            csv_file = open(filename, 'r')
        except FileNotFoundError:
            return False

        for line in csv_file:
            csv_line = tuple(line.split(","))
            if csv_line[3] == 'TEMP':
                temp_line = csv_line
                day = int(temp_line[0])
                time = math.floor((float(temp_line[1]) * 24))
                sensors = int(temp_line[2])
                temp = float(temp_line[4])
                data_tuple = (day, time, sensors, temp)
                self._data_set.append(tuple(data_tuple))
        return True

    def get_summary_statistics(self, active_sensors):
        if self._data_set is None:
            return None
        temperature = [item[3] for item in self._data_set
                       if item[2] in active_sensors]
        if len(temperature) == 0:
            return None
        return min(temperature), \
               max(temperature), \
               sum(temperature)/len(temperature)
        # tuple of min temp^, max temp^, and avg temp^ (like in next method)

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        if self._data_set is None:
            return None
        temperature = [item[3] for item in self._data_set
                       if item[0] == day
                       and item[1] == time
                       and item[2] in active_sensors]
        if len(temperature) == 0:
            return None
        return sum(temperature)/len(temperature)

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if self._data_set is None:
            return None
        else:
            return 0

    def get_loaded_temps(self):
        if not self._data_set:
            return False
        else:
            return int(len(self._data_set))


def main():
    current_set = TempDataset()

    print_header()
    while True:
        print_menu()
        print(current_set.get_avg_temperature_day_time(active_sensors, 5, 7))
        try:
            user_response = int(input("What is your choice?: "))
            if user_response == 1:
                new_file(current_set)
            elif user_response == 2:
                choose_units()
            elif user_response == 3:
                change_filter(sensor_list, active_sensors)
            elif user_response == 4:
                print_summary_statistics(current_set, active_sensors)
            elif user_response == 5:
                print_temp_by_day_time(current_set, None)
            elif user_response == 6:
                print_histogram(current_set, None)
            else:
                if user_response > 7 or user_response < 1:
                    print('Invalid choice\n')
                if user_response == 7:
                    print('Thank you for using the STEM Center Temperature Project')
                    break
        except ValueError:
            print('*** Please enter a number only ***\n')


if __name__ == "__main__":
    main()

'''Output:
/Users/shreyaraj/PycharmProjects/PostMidtermAssignments/venv/bin/python /Users/shreyaraj/PycharmProjects/PostMidtermAssignments/Assignment10.py
STEM Center Temperature Project
Shreya Raj

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice?: 4
Please load data file and make sure at least one sensor is active
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice?: 1
Please enter the filename of the new data set:
Temperatures2017-08-06.csv
Loaded 11724 samples.
Please provide a 3 to 20 character name for the data set:
My Data Set
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice?: 4
Summary statistics for My Data Set 

Minimum Temperature: 16.55 C
Maximum Temperature: 28.42 C
Average Temperature: 21.46844848174671 C
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice?: 2
Current units in Celsius 

Choose your preferred units:
0 : Celsius
1 : Fahrenheit
2 : Kelvin
Which unit do you choose?
1
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice?: 4
Summary statistics for My Data Set 

Minimum Temperature: 61.790000000000006 F
Maximum Temperature: 83.156 F
Average Temperature: 70.64320726714408 F
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice?: 3
 
4201 : Foundations Lab   [ACTIVE]
4204 : CS Lab   [ACTIVE]
4205 : Tiled Room   [ACTIVE]
4213 : STEM Center   [ACTIVE]
4218 : Workshop Room   [ACTIVE]
Out : Outside   [ACTIVE]
 
Type the sensor to toggle (e.g. 4201) or x to end: 
4201
 
4201 : Foundations Lab
4204 : CS Lab   [ACTIVE]
4205 : Tiled Room   [ACTIVE]
4213 : STEM Center   [ACTIVE]
4218 : Workshop Room   [ACTIVE]
Out : Outside   [ACTIVE]
 
Type the sensor to toggle (e.g. 4201) or x to end: 
4204
 
4201 : Foundations Lab
4204 : CS Lab
4205 : Tiled Room   [ACTIVE]
4213 : STEM Center   [ACTIVE]
4218 : Workshop Room   [ACTIVE]
Out : Outside   [ACTIVE]
 
Type the sensor to toggle (e.g. 4201) or x to end: 
x
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

19.910638297872342
What is your choice?: 4
Summary statistics for My Data Set 

Minimum Temperature: 61.790000000000006 F
Maximum Temperature: 83.156 F
Average Temperature: 70.12994335289653 F
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

19.910638297872342
What is your choice?: 3
 
4201 : Foundations Lab
4204 : CS Lab
4205 : Tiled Room   [ACTIVE]
4213 : STEM Center   [ACTIVE]
4218 : Workshop Room   [ACTIVE]
Out : Outside   [ACTIVE]
 
Type the sensor to toggle (e.g. 4201) or x to end: 
4205
 
4201 : Foundations Lab
4204 : CS Lab
4205 : Tiled Room
4213 : STEM Center   [ACTIVE]
4218 : Workshop Room   [ACTIVE]
Out : Outside   [ACTIVE]
 
Type the sensor to toggle (e.g. 4201) or x to end: 
4213
 
4201 : Foundations Lab
4204 : CS Lab
4205 : Tiled Room
4213 : STEM Center
4218 : Workshop Room   [ACTIVE]
Out : Outside   [ACTIVE]
 
Type the sensor to toggle (e.g. 4201) or x to end: 
4218
 
4201 : Foundations Lab
4204 : CS Lab
4205 : Tiled Room
4213 : STEM Center
4218 : Workshop Room
Out : Outside   [ACTIVE]
 
Type the sensor to toggle (e.g. 4201) or x to end: 
Out
 
4201 : Foundations Lab
4204 : CS Lab
4205 : Tiled Room
4213 : STEM Center
4218 : Workshop Room
Out : Outside
 
Type the sensor to toggle (e.g. 4201) or x to end: 
x
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice?: 4
Please load data file and make sure at least one sensor is active
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice?: 7
Thank you for using the STEM Center Temperature Project

Process finished with exit code 0
'''
