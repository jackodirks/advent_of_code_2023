import re
import itertools

def non_overlap_and_monotonous_check(product, lengths):
    for index in range(len(product)):
        for other_index in range(index + 1, len(product)):
            if product[index] + lengths[index] >= product[other_index]:
                return False
    return True

def position_is_covered_by_product(product, lengths, pos):
    for index in range(len(product)):
        if product[index] <= pos and product[index] + lengths[index] > pos:
            return True
    return False

def get_legal_combinations(record, numbers, possible_positions):
    assert len(numbers) > 1
    hashtag_positions = [i for i in range(len(record)) if record[i] == "#"]
    total_legal = 0
    for prod in itertools.product(*possible_positions):
        # None of the elements should overlap, and they should be monotonically increasing
        if not non_overlap_and_monotonous_check(prod, numbers):
            continue
        if not all(position_is_covered_by_product(prod, numbers, pos) for pos in hashtag_positions):
            continue
        total_legal += 1
    assert total_legal > 0
    return total_legal

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]

    records = []
    numbers = []
    for line in lines:
        match = re.match("([^\s]+)\s+([^\s]+)", line)
        records.append(match.group(1))
        numbers.append([int(x) for x in match.group(2).split(",")])

    total = 0
    for i in range(len(records)):
        rec = records[i]
        nums = numbers[i] 
        possible_pos_list = []
        for index in range(len(nums)):
            start_pos = 0
            if index > 0:
                start_pos = sum(nums[:index]) + len(nums[:index])
                #start_pos = min(possible_pos_list[index - 1]) + nums[index - 1]
            end_pos = len(rec)
            if index < len(nums) - 1:
                end_pos -= sum(nums[index+1:]) + len(nums[index+1:])
            end_pos = min(end_pos, len(rec) - nums[index] + 1)
            length = nums[index]
            position_list = []
            for pos in range(start_pos, end_pos):
                if "." in rec[pos:pos+length]:
                    continue
                if pos > 0 and rec[pos - 1] == "#":
                    continue
                if pos + length < len(rec) and rec[pos+length] == "#":
                    continue
                position_list.append(pos)
            possible_pos_list.append(position_list)
        total += get_legal_combinations(rec, nums, possible_pos_list)
    print(total)
            
