import re
import os

def parse_text(file_path):
    with open(file_path, 'r') as file:
        line = file.read()
    return line

def get_cost(line):
    return sum(x*y for x, y in [[int(number) for number in re.findall(r"\d+", match)] for match in re.findall(r"mul\(\d+,\d+\)", line)])
        
def main():
    file_path = os.path.join(os.path.abspath(os.getcwd()), 'data.txt')
    print(get_cost(parse_text(file_path)))
    
if __name__ == '__main__':
    main()