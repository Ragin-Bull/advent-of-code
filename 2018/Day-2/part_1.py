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
        twos=0
        threes=0

        for word in data:
            df = defaultdict(int)
            two_found=0
            three_found=0

            for letter in word:
                df[letter]+=1

            for key, value in df.items():
                if df[key]==2:
                    two_found+=1
                elif df[key]==3:
                    three_found+=1

            if two_found:
                twos+=1

            if three_found:
                threes+=1

        print(twos*threes)

    except FileNotFoundError as e:
        print(e)
