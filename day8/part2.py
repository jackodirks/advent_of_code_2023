import re
import math
import itertools

def determine_cycle(instructions, node_dict, start_node_key):
    index_node_pairs = {i : [] for i in range(len(instructions))}
    index_cycle_step_pairs = {i : [] for i in range(len(instructions))}
    start_node = node_dict[start_node_key]
    cycle_length = 0
    end_counts = []
    for index in itertools.cycle(range(len(instructions))):
        instruction = instructions[index]
        if instruction == "L":
            start_node_key = start_node[0]
        else:
            start_node_key = start_node[1]
        start_node = node_dict[start_node_key]
        cycle_length += 1
        index_cycle_step_pairs[index].append(cycle_length)
        if start_node_key[-1] == "Z":
            end_counts.append(cycle_length)
        if start_node_key in index_node_pairs[index]:
            relevant_set = index_cycle_step_pairs[index]
            break
        index_node_pairs[index].append(start_node_key)
    return end_counts[0], relevant_set[0], relevant_set[-1]

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
    lines_iter = iter(lines)
    instructions = next(lines_iter)
    next(lines_iter)
    node_dict = {match.group(1): (match.group(2), match.group(3)) for match in [re.match("([^\s]+)\s+=\s+\(([^\s]+),\s+([^\s]+)\)", line) for line in lines_iter]}
    active_nodes = [k for k in node_dict.keys() if k[-1] == "A"]
    data_points = [(determine_cycle(instructions, node_dict, node)) for node in active_nodes]
    steps = [cycle_end - cycle_start for _, cycle_start, cycle_end in data_points]
    print(math.lcm(*steps))
