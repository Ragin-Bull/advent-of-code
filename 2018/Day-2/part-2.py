import os
import sys
from collections import defaultdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../utils")))

from parse_file import return_array_of_strings

if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "data.txt")

    try:
        data = return_array_of_strings(input_file_path)
        num = len(data)
        matching_indices = [0, 1]

        for i in range(num):
            for j in range(i+1, num):
                mismatches=0
                for k in range(len(data[i])):
                    if data[i][k] != data[j][k]:
                        mismatches+=1

                if mismatches == 1:
                    matching_indices = [i, j]

        x = matching_indices[0]
        y = matching_indices[1]



    except FileNotFoundError as e:
        print(e)
