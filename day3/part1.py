import re

def _num_is_partnum(partslist, y_coord, x_start_coord, x_end_coord):

    def _check_num_with_line(lineparts, x_start_coord, x_end_coord):
        for index in range(x_start_coord - 1, x_end_coord + 1):
            if index in lineparts:
                return True
        return False

    if y_coord - 1 >= 0:
        if _check_num_with_line(partslist[y_coord - 1], x_start_coord, x_end_coord):
            return True;
    if y_coord + 1 < len(partslist):
        if _check_num_with_line(partslist[y_coord + 1], x_start_coord, x_end_coord):
            return True;

    return _check_num_with_line(partslist[y_coord], x_start_coord, x_end_coord)

if __name__ == "__main__":
    with open("input") as file:
        # Iteration one, get an index for every part
        partslist = []
        lines = [line.rstrip() for line in file]
        for line in lines:
            lineparts = []
            for match in re.finditer("[^.\d]", line):
                lineparts.append(match.start(0))
            partslist.append(lineparts)

        # Iteration two, find the numbers see if they hit parts
        y_coord = 0
        totalsum = 0
        for line in lines:
            for match in re.finditer("\d+", line):
                if _num_is_partnum(partslist, y_coord, match.start(0), match.end(0)):
                    totalsum += int(match.group(0))
            y_coord += 1
        print(totalsum)
