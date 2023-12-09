import re
import itertools

def make_prediction(history_line):
    lines = [history_line]
    while not all(i == 0 for i in lines[-1]):
        lines.append([j - i for i,j in zip(lines[-1], lines[-1][1:])])
    prediction = 0
    for line in lines:
        if len(line) > 0:
            prediction += line[-1]
    return prediction

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]

    history_lines = []
    for line in lines:
        history_lines.append([int(match.group(0)) for match in re.finditer("-?\d+", line)])

    print(sum([make_prediction(l) for l in history_lines]))
