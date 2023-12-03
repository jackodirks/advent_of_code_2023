import re

def _get_min(line, re_str):
    num_list = [0]
    for m in re.finditer(re_str, line):
        num_list.append(int(m.group(1)))
    return max(num_list)

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
        total = 0
        for line in lines:
            min_red = _get_min(line, "(\d+) red")
            min_green = _get_min(line, "(\d+) green")
            min_blue = _get_min(line, "(\d+) blue")
            total += min_red * min_green * min_blue
        print(total)
