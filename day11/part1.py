import itertools

def find_galaxy_distance(row_costs, col_costs, galaxy_a, galaxy_b):
    horizontal_costs = 0
    for i in range(min(galaxy_a[0], galaxy_b[0]) + 1, max(galaxy_a[0], galaxy_b[0]) + 1):
        horizontal_costs += col_costs[i]
    vertical_costs = 0
    for i in range(min(galaxy_a[1], galaxy_b[1]) + 1, max(galaxy_a[1], galaxy_b[1]) + 1):
        vertical_costs += row_costs[i]
    return horizontal_costs + vertical_costs

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]

    galaxy_locations = []
    y_coord = 0
    for line in lines:
        for x_coord in range(len(line)):
            if line[x_coord] == "#":
                galaxy_locations.append((x_coord, y_coord))
        y_coord += 1

    row_costs = [1]*len(lines[0])
    for index in range(len(lines)):
        if all(c == "." for c in lines[index]):
            row_costs[index] = 2
    col_costs = [1]*len(lines)
    for index in range(len(lines[0])):
        col = [line[index] for line in lines]
        if all(c == "." for c in col):
            col_costs[index] = 2

    total_cost = 0
    for a,b in itertools.combinations(galaxy_locations, 2):
        total_cost += find_galaxy_distance(row_costs, col_costs, a, b)
    print(total_cost)

