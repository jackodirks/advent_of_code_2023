import re

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]

    lines_iter = iter(lines)
    instructions = next(lines_iter)
    next(lines_iter)

    node_dict = {}

    for line in lines_iter:
        match = re.match("([^\s]+)\s+=\s+\(([^\s]+),\s+([^\s]+)\)", line)
        node_dict[match.group(1)] = (match.group(2), match.group(3))

    node = node_dict["AAA"]

    stop = False
    step_count = 0
    while not stop:
        for instruction in instructions:
            if instruction == "L":
                key = node[0]
            else:
                key = node[1]
            node = node_dict[key]
            step_count += 1
            if key == "ZZZ":
                stop = True
                break
    print(step_count)


