import os
import re


def parse_the_file(file_path):
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

def delete_element(arr, i):
    arr = arr[:]
    arr.pop(i)
    return arr

def check(arr):
    return bool(arr and (check_seq(arr, 0) or check_seq(arr, 1)) and check_max_diff(arr)) 


if __name__ == "__main__":
    file_path = os.path.join(os.path.abspath(os.getcwd()), "data.txt")

    reports = parse_the_file(file_path)
    safe_reports = 0
    
    for report in reports:
        ultimate_flag = 0
        ultimate_flag = check(report)
        safe_reports+=(1 and ultimate_flag)
        
        if not ultimate_flag:
            num = len(report)
            for i in range(num):
                updated_report = delete_element(report, i)
                ultimate_flag = check(updated_report)
                
                if ultimate_flag:
                    safe_reports+=1
                    break



    print(safe_reports)
