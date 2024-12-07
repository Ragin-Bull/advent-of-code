import re
import os

def parse_text(file_path):
    with open(file_path, 'r') as file:
        line = file.read()
    return line

def preprocess(line):
    # First remove the substring between don't() and do()
    line = re.sub(r"don't\(\).*?do\(\)", '', line, flags=re.DOTALL) # DOTALL includes all characters including \n
    
    # Secondly remove the part between don't() and end of the string
    line = re.sub(r"don't\(\).*?$", '', line, flags=re.DOTALL)
    
    return line  

def get_cost(line):
    return sum(x*y for x, y in [[int(number) for number in re.findall(r"\d+", match)] for match in re.findall(r"mul\(\d+,\d+\)", preprocess(line))])   


def main():
    file_path = os.path.join(os.path.abspath(os.getcwd()), 'data.txt')
    print(get_cost(parse_text(file_path)))
    
    
if __name__ == '__main__':
    main()