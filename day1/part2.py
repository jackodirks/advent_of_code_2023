import re

_num_lut = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9",
        "zero" : "0"
        }

if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
        val = 0
        for line in lines:
            nums_found = []
            for k,v in _num_lut.items():
                for m in re.finditer(k, line):
                    nums_found.append((m.start(), v))
                for m in re.finditer(v, line):
                    nums_found.append((m.start(), v))
            nums_found.sort(key=lambda tup: tup[0])
            num = int(f'{nums_found[0][1]}{nums_found[-1][1]}')
            val += num
        print(val)
