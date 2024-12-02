import os
import re


def parse_stuff(file_path):
    with open(file_path) as file:
        return [[int(match) for match in re.findall(r"\S+", line)] for line in file.read().split("\n")]


def check_seq(arr, flag):
    for i in range(1, len(arr)):
        if flag and arr[i] <= arr[i - 1]:
            return 0
        elif flag == 0 and arr[i] >= arr[i-1]:
            return 0
    return 1


def check_max_diff(arr):
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) < 1 or abs(arr[i] - arr[i - 1]) > 3:
            return 0

    return 1


if __name__ == "__main__":
    file_path = os.path.join(os.path.abspath(os.getcwd()), "data.txt")

    reports = parse_stuff(file_path)
    safe_reports = 0

    for report in reports:
        if report:
            safe_reports += (check_seq(report, 0) or check_seq(report, 1)) and check_max_diff(report)

    print(safe_reports)
