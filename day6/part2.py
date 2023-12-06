import re
import math

def get_race_distance(maxtime, time):
    return (maxtime - time)*time

def get_inner_bounds(time, distance):
    det = math.sqrt(time**2 - 4*distance)
    a = (-time+det)/-2
    b = (-time-det)/-2
    a,b = math.ceil(min(a,b)), math.floor(max(a,b))
    if get_race_distance(time, a) <= distance:
        a += 1
    if get_race_distance(time, b) <= distance:
        b -= 1
    return a, b

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
    lines_iter = iter(lines)
    time = int("".join([match.group(0) for match in re.finditer("\d+", next(lines_iter))]))
    distance = int("".join([match.group(0) for match in re.finditer("\d+", next(lines_iter))]))

    a, b = get_inner_bounds(time, distance)
    print((b - a) + 1)

