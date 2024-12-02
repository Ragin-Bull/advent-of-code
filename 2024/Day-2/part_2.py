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


def check_seq(arr, flag):
    num = len(arr)

    for i in range(1, num):
        if flag and arr[i] <= arr[i - 1]:
            return 0
        elif flag == 0 and arr[i] >= arr[i-1]:
            return 0
    return 1


def check_max_diff(arr):
    num = len(arr)

    for i in range(1, num):
        if abs(arr[i] - arr[i - 1]) < 1 or abs(arr[i] - arr[i - 1]) > 3:
            return 0

    return 1

def remove_it(arr, i):
    arr = arr[:]
    arr.pop(i)
    return arr


if __name__ == "__main__":
    _file_path = os.path.join(os.path.abspath(os.getcwd()), "data.txt")

    reports = parse_stuff(_file_path)
    safe_reports = 0
    for report in reports:
        if report:
            ultimate_flag = 0
            ultimate_flag = (check_seq(report, 0) or check_seq(report, 1)) and check_max_diff(report)
            if ultimate_flag:
                safe_reports+=1
                continue
            else:
                num = len(report)
                for i in range(num):
                    updated_report = remove_it(report, i)
                    if updated_report:
                        ultimate_flag = (check_seq(updated_report, 0) or check_seq(updated_report, 1)) and check_max_diff(updated_report)
                        if ultimate_flag:
                            safe_reports+=1
                            break



    print(safe_reports)
