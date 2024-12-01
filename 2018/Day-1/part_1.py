import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../utils")))

from parse_file import return_array_of_strings

input_file_path = os.path.join(os.path.dirname(__file__), "data.txt")

try:
    data = return_array_of_strings(input_file_path)
    num = len(data)
    initial_frequency = 0

    for i in range(num):
        initial_frequency = int(data[i]) + initial_frequency

    print(initial_frequency)
except FileNotFoundError as e:
    print(e)
