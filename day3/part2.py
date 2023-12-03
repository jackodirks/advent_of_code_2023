import re

def _get_hitcount_gearratio(numlist, y_coord, x_coord):

    def _check_x_coord_with_line(linenums, x_coord):
        hitcount = 0
        gearratio = 1
        for start, end, num in linenums:
            if start - 1 <= x_coord and end >= x_coord:
                hitcount += 1
                gearratio *= num
        return hitcount, gearratio

    hitcount = 0
    gearratio = 1
    if y_coord - 1 >= 0:
        _h, _g = _check_x_coord_with_line(numlist[y_coord - 1], x_coord)
        hitcount += _h
        gearratio *= _g

    if y_coord + 1 < len(numlist):
        _h, _g = _check_x_coord_with_line(numlist[y_coord + 1], x_coord)
        hitcount += _h
        gearratio *= _g

    _h, _g = _check_x_coord_with_line(numlist[y_coord], x_coord)
    hitcount += _h
    gearratio *= _g

    return hitcount, gearratio

if __name__ == "__main__":
    with open("input") as file:
        # Iteration one, get an tuple containing (startindex, endindex, number) for every number on every line
        numlist = []
        lines = [line.rstrip() for line in file]
        for line in lines:
            linenums = []
            for match in re.finditer("\d+", line):
                linenums.append((match.start(0), match.end(0), int(match.group(0))))
            numlist.append(linenums)

        # Iteration two, find the asterixes, check how many numbers they hit and what their gearratio would be
        y_coord = 0
        totalsum = 0
        for line in lines:
            for match in re.finditer("\*", line):
                hitcount, gearratio = _get_hitcount_gearratio(numlist, y_coord, match.start(0))
                if hitcount == 2:
                    totalsum += gearratio
            y_coord += 1
        print(totalsum)
