import re

_RED_COUNT = 12
_GREEN_COUNT = 13
_BLUE_COUNT = 14

def subset_valid(substr):
    red_count = 0
    match = re.search("(\d+) red", substr)
    if match:
        red_count = int(match.group(1))

    green_count = 0
    match = re.search("(\d+) green", substr)
    if match:
        green_count = int(match.group(1))

    blue_count = 0
    match = re.search("(\d+) blue", substr)
    if match:
        blue_count = int(match.group(1))

    return red_count <= _RED_COUNT and green_count <= _GREEN_COUNT and blue_count <= _BLUE_COUNT

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
        total = 0
        for line in lines:
            game_id = int(re.search("^Game (\d+):", line).group(1))
            line = re.sub("^Game \d+:", "", line).strip()
            valid = True
            for substr in line.split(";"):
                substr = substr.strip().rstrip()
                if not subset_valid(substr):
                    valid = False
                    break
            if valid:
                total += game_id
        print(total)
