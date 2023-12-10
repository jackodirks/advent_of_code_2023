import re

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
                direction_dict[(x_coord, y_coord)] = [(x_coord, y_coord - 1), (x_coord, y_coord + 1)]
                continue
            if direction == "-":
                direction_dict[(x_coord, y_coord)] = [(x_coord-1, y_coord), (x_coord+1, y_coord)]
                continue
            if direction == "L":
                direction_dict[(x_coord, y_coord)] = [(x_coord, y_coord-1), (x_coord+1, y_coord)]
                continue
            if direction == "J":
                direction_dict[(x_coord, y_coord)] = [(x_coord, y_coord-1), (x_coord-1, y_coord)]
                continue
            if direction == "7":
                direction_dict[(x_coord, y_coord)] = [(x_coord, y_coord+1), (x_coord-1, y_coord)]
                continue
            if direction == "F":
                direction_dict[(x_coord, y_coord)] = [(x_coord, y_coord+1), (x_coord+1, y_coord)]
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

    previous_position = start_point
    #w.l.o.g.
    current_position = start_directions[0]
    current_steps = 1
    while current_position != start_point:
        possible_next_positions = direction_dict[current_position]
        if possible_next_positions[0] != previous_position:
            key = 0
        else:
            key = 1
        previous_position = current_position
        current_position = possible_next_positions[key]
        current_steps += 1

    print(current_steps//2)
