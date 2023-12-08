import re
import itertools

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
    instructions = lines[0]
    node_dict = {match.group(1): (match.group(2), match.group(3)) for match in [re.match("([^\s]+)\s+=\s+\(([^\s]+),\s+([^\s]+)\)", line) for line in lines[2:]]}
    node = node_dict["AAA"]
    step_count = 0
    for instruction in itertools.cycle(instructions):
        if instruction == "L":
            key = node[0]
        else:
            key = node[1]
        node = node_dict[key]
        step_count += 1
        if key == "ZZZ":
            break
    print(step_count)


