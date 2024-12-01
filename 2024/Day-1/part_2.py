import os
import re
from collections import defaultdict


def parse_stuff(file_path):
    with open(file_path, "r") as file:
        lines = file.read().split("\n")

    array_a = []
    array_b = []

    for line in lines:
        matches = re.findall(r"\S+", line)
        if matches:
            array_a.append(int(matches[0]))
            array_b.append(int(matches[1]))

    return array_a, array_b


def get_final_ans(array_a, array_b):
    similarity = 0
    df = defaultdict(int)

    for element in array_b:
        df[element] += 1

    for element in array_a:
        similarity += element * df[element]

    return similarity


if __name__ == "__main__":
    _file_path = os.path.join(os.path.abspath(os.getcwd()), "data.txt")
    array_a, array_b = parse_stuff(_file_path)

    array_a.sort()
    array_b.sort()

    # print(array_a)
    # print(array_b)

    print(get_final_ans(array_a, array_b))
