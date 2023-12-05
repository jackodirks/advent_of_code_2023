import re
import math

def next_wrapper(any_iter):
    try:
        return next(any_iter)
    except StopIteration:
        return None

def post_process(mapping):
    ret_mapping = []
    map_iter = iter(mapping)
    elem = next_wrapper(map_iter)
    if elem[1] > 0:
        ret_mapping.append((0, 0, elem[1]))
    ret_mapping.append(elem)
    current_end = elem[1] + elem[2]
    elem = next_wrapper(map_iter)
    while elem is not None:
        if elem[1] != current_end:
            ret_mapping.append((current_end, current_end, elem[1] - current_end))
        current_end = elem[1] + elem[2]
        ret_mapping.append(elem)
        elem = next_wrapper(map_iter)
    end_elem = mapping[-1]
    end_value = end_elem[1] + end_elem[2]
    ret_mapping.append((end_value, end_value, math.inf))
    return ret_mapping

def find_value(reverse_mappings, index, search_start, search_rlen):
    if index >= len(reverse_mappings):
        return search_start
    mappings = reverse_mappings[index]
    for dest, src, rlen in mappings:
        orig_dest, orig_src, orig_rlen = dest, src, rlen
        if dest < search_start + search_rlen and dest + rlen > search_start:
            if dest > search_start:
                search_rlen += search_start - dest
                search_start = dest
            if search_start > dest:
                rlen += dest - search_start
            translated_search_start = search_start + (src - dest)
            translated_search_rlen = min(rlen, search_rlen)
            val = find_value(reverse_mappings, index + 1, translated_search_start, translated_search_rlen)
            if val != -1:
                return val
    return -1

def get_mapping(lines_iter):
    mappings = []
    line = next_wrapper(lines_iter)
    while line is not None and line != "":
        match = re.match("(\d+)\s+(\d+)\s+(\d+)", line)
        mappings.append((int(match.group(1)), int(match.group(2)), int(match.group(3))))
        line = next_wrapper(lines_iter)
    mappings.sort(key=lambda tup : tup[1])
    mappings = post_process(mappings)
    mappings.sort(key=lambda tup : tup[0])
    return mappings

def apply_mapping(mapping, val):
    for dest, src, rlen in mapping:
        if val >= src and val < src + rlen:
            return val + (dest - src)
    return val

def map_seed_to_location(mappings, val):
    for mapping in mappings:
        val = apply_mapping(mapping, val)
    return val

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
    lines_iter = iter(lines)
    # First line contains my seeds
    seeds = [(int(match.group(1)), int(match.group(2))) for match in re.finditer("(\d+)\s+(\d+)", next(lines_iter))]
    # Flush out one last empty line..
    next_wrapper(lines_iter)
    seeds_as_mapping = [(val, val, rlen) for val, rlen in seeds]
    seeds_as_mapping.sort(key=lambda tup : tup[0])
    all_mappings = [seeds_as_mapping]
    while next_wrapper(lines_iter) is not None:
        all_mappings.append(get_mapping(lines_iter))

    reverse_mappings = all_mappings.copy()
    reverse_mappings.reverse()
    for mapping in reverse_mappings[0]:
        val = find_value(reverse_mappings, 1, mapping[1], mapping[2])
        if val > 0:
            print(map_seed_to_location(all_mappings[1:], val))
            break

