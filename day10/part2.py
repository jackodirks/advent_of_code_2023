import re
import copy

_heading_to_lr = {
        (1, 0) : ((0, -1), (0, 1)),
        (-1, 0) : ((0, 1), (0, -1)),
        (0, 1) : ((1, 0), (-1, 0)),
        (0, -1) : ((-1, 0), (1, 0))}

def map_contains_underscore(_map):
    for line in _map:
        for c in line:
            if c == "_":
                return True
    return False

def print_map(total_map):
    for line in total_map:
        for e in line:
            print(e, end="")
        print("\n", end="")


if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]

    direction_dict = {}
    start_point = (0,0)

    y_coord = 0
    for line in lines:
        for x_coord in range(len(line)):
            direction = line[x_coord]
            if direction == "|":
                direction_dict[(x_coord, y_coord)] = [(x_coord, y_coord - 1), (x_coord, y_coord + 1), "\u2503"]
                continue
            if direction == "-":
                direction_dict[(x_coord, y_coord)] = [(x_coord-1, y_coord), (x_coord+1, y_coord), "\u2501"]
                continue
            if direction == "L":
                direction_dict[(x_coord, y_coord)] = [(x_coord, y_coord-1), (x_coord+1, y_coord), "\u2517"]
                continue
            if direction == "J":
                direction_dict[(x_coord, y_coord)] = [(x_coord, y_coord-1), (x_coord-1, y_coord), "\u251B"]
                continue
            if direction == "7":
                direction_dict[(x_coord, y_coord)] = [(x_coord, y_coord+1), (x_coord-1, y_coord), "\u2513" ]
                continue
            if direction == "F":
                direction_dict[(x_coord, y_coord)] = [(x_coord, y_coord+1), (x_coord+1, y_coord), "\u250F"]
                continue
            if direction == "S":
                start_point = (x_coord, y_coord)
                continue
        y_coord += 1

    # Determine start directions
    start_directions = []
    for offset in (-1, 1):
        check_coords = (start_point[0], start_point[1] + offset)
        if check_coords in direction_dict and start_point in direction_dict[check_coords]:
            start_directions.append(check_coords)
        check_coords = (start_point[0] + offset, start_point[1])
        if check_coords in direction_dict and start_point in direction_dict[check_coords]:
            start_directions.append(check_coords)
    direction_dict[start_point] = [start_directions[0], start_directions[1], "s"]

    previous_position = start_point
    #w.l.o.g.
    current_position = start_directions[0]
    elements_on_path = [start_point]
    left_elements = []
    right_elements = []
    while current_position != start_point:
        heading = (previous_position[0] - current_position[0], previous_position[1] - current_position[1])
        left_offset, right_offset = _heading_to_lr[heading]
        element_left = tuple(map(sum,zip(current_position,left_offset)))
        left_elements.append(element_left)
        element_right = tuple(map(sum,zip(current_position,right_offset)))
        right_elements.append(element_right)
        elements_on_path.append(current_position)
        possible_next_positions = direction_dict[current_position]
        if possible_next_positions[0] != previous_position:
            key = 0
        else:
            key = 1
        previous_position = current_position
        current_position = possible_next_positions[key]
        new_heading = (previous_position[0] - current_position[0], previous_position[1] - current_position[1])
        if (heading != new_heading):
            heading = new_heading
            left_offset, right_offset = _heading_to_lr[heading]
            element_left = tuple(map(sum,zip(previous_position,left_offset)))
            if all(i >= 0 for i in element_left):
                left_elements.append(element_left)
            element_right = tuple(map(sum,zip(previous_position,right_offset)))
            if all(i >= 0 for i in element_right):
                right_elements.append(element_right)

    total_map = [ ["_"]*len(lines[0]) for i in range(len(lines))]

    for l in left_elements:
        try:
            total_map[l[1]][l[0]] = "l"
        except IndexError:
            pass

    for r in right_elements:
        try:
            total_map[r[1]][r[0]] = "r"
        except IndexError:
            pass

    for e in elements_on_path:
        total_map[e[1]][e[0]] = direction_dict[e][2]

    print("Pre infection spread map")
    print_map(total_map)

    prev_map = copy.deepcopy(total_map)
    iterations = 0
    while map_contains_underscore(total_map):
        for y_coord in range(len(total_map)):
            for x_coord in range(len(total_map[0])):
                if total_map[y_coord][x_coord] == "_":
                    my_coord = (y_coord, x_coord)
                    for heading in _heading_to_lr.keys():
                        elem_coord = tuple(map(sum,zip(my_coord,heading)))
                        try:
                            if total_map[elem_coord[0]][elem_coord[1]] == "l":
                                total_map[y_coord][x_coord] = "l"
                                break
                            if total_map[elem_coord[0]][elem_coord[1]] == "r":
                                total_map[y_coord][x_coord] = "r"
                                break
                        except IndexError:
                            pass
        assert total_map != prev_map
        prev_map = copy.deepcopy(total_map)

    l_count = 0
    r_count = 0
    for line in total_map:
        for c in line:
            if c == "l":
                l_count += 1
            if c == "r":
                r_count += 1

    print("Final map")
    print_map(total_map)
    print(min(l_count, r_count))
