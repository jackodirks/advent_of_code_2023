import re

def next_wrapper(any_iter):
    try:
        return next(any_iter)
    except StopIteration:
        return None

def get_mapping(lines_iter):
    mappings = []
    line = next_wrapper(lines_iter)
    while line is not None and line != "":
        match = re.match("(\d+)\s+(\d+)\s+(\d+)", line)
        mappings.append((int(match.group(1)), int(match.group(2)), int(match.group(3))))
        line = next_wrapper(lines_iter)
    return mappings

def apply_mapping(mapping, val):
    for dest, src, rlen in mapping:
        if val >= src and val < src + rlen:
            return val + (dest - src)
    return val

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
    lines_iter = iter(lines)
    # First line contains my seeds
    seeds = [int(match.group(0)) for match in re.finditer("\d+", next(lines_iter))]
    # Flush out one last empty line..
    next_wrapper(lines_iter)
    all_mappings = []
    while next_wrapper(lines_iter) is not None:
        all_mappings.append(get_mapping(lines_iter))

    locations = []
    for val in seeds:
        for mapping in all_mappings:
            val = apply_mapping(mapping, val)
        locations.append(val)
    print(min(locations))
