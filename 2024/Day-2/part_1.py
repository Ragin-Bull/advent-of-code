import os
import re


def parse_stuff(file_path):
    with open(file_path) as file:
        lines = file.read().split("\n")

    reports = []

    for line in lines:
        matches = re.findall(r"\S+", line)
        each_entry = []
        for match in matches:
            each_entry.append(int(match))
        reports.append(each_entry)

    return reports


def check_inc_seq(arr):
    num = len(arr)

    for i in range(1, num):
        if arr[i] <= arr[i - 1]:
            return 0
    return 1


def check_dec_seq(arr):
    num = len(arr)

    for i in range(1, num):
        if arr[i] >= arr[i - 1]:
            return 0

    return 1


def check_max_diff(arr):
    num = len(arr)

    for i in range(1, num):
        if abs(arr[i] - arr[i - 1]) < 1 or abs(arr[i] - arr[i - 1]) > 3:
            return 0

    return 1


if __name__ == "__main__":
    _file_path = os.path.join(os.path.abspath(os.getcwd()), "data.txt")

    reports = parse_stuff(_file_path)
    safe_reports = 0

    for report in reports:
        if report:
            flag = 0

            flag = (check_inc_seq(report) or check_dec_seq(report)) and check_max_diff(
                report
            )

            safe_reports += flag

    print(safe_reports)
