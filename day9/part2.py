import re
import itertools

def make_prediction(history_line):
    lines = [history_line]
    while not all(i == 0 for i in lines[-1]):
        lines.append([j - i for i,j in zip(lines[-1], lines[-1][1:])])
    prediction = 0
    for line in reversed(lines):
        prediction = line[0] - prediction
    return prediction

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]

    history_lines = [[int(match.group(0)) for match in re.finditer("-?\d+", line)] for line in lines]

    print(sum([make_prediction(l) for l in history_lines]))
