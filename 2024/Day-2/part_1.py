import os
import re


def parse_the_file(file_path):
    with open(file_path) as file:
        return [[int(match) for match in re.findall(r"\S+", line)] for line in file.read().split("\n")]


def check_seq(arr, flag):
    return all([arr[i]>arr[i-1] if flag else arr[i]<arr[i-1] for i in range(1, len(arr))])


def check_max_diff(arr):
    return all([1 <= abs(arr[i]-arr[i-1]) <= 3 for i in range(1, len(arr))])


if __name__ == "__main__":
    file_path = os.path.join(os.path.abspath(os.getcwd()), "data.txt")

    reports = parse_the_file(file_path)
    safe_reports = 0

    for report in reports:
        if report:
            safe_reports += (check_seq(report, 0) or check_seq(report, 1)) and check_max_diff(report)

    print(safe_reports)
