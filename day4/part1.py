import re

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
    pointscount = 0
    for line in lines:
        line = re.sub("^Card\s*\d+:", "", line).strip()
        winning_numbers_substring = re.match("(^.*)\|", line).group(1).rstrip()
        numbers_i_have_substring = re.match(".*\|(.*$)", line).group(1).strip()
        winning_numbers = [int(match.group(0)) for match in re.finditer("\d+", winning_numbers_substring)]
        numbers_i_have = [int(match.group(0)) for match in re.finditer("\d+", numbers_i_have_substring)]
        winning_numbers_i_have = len(set(winning_numbers) & set(numbers_i_have))
        if winning_numbers_i_have > 0:
            pointscount += 2**(winning_numbers_i_have - 1)
    print(pointscount)

