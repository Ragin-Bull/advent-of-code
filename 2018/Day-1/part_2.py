import os
import sys
from collections import defaultdict
from itertools import cycle

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../utils")))

from parse_file import return_array_of_strings

input_file_path = os.path.join(os.path.dirname(__file__), "data.txt")

try:
    data = return_array_of_strings(input_file_path)
    num = len(data)
    initial_frequency = 0
    df = defaultdict(int)
    df[0]=1

    for element in cycle(data):
        initial_frequency = int(element) + initial_frequency
        df[initial_frequency]+=1

        if(df[initial_frequency]>=2):
            print(initial_frequency)
            break

except FileNotFoundError as e:
    print(e)
