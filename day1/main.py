if __name__ == "__main__":
    with open("input") as file:
        lines = [line.rstrip() for line in file]
        val = 0
        for line in lines:
            digits = [x for x in line if x.isdigit()]
            num = int(f'{digits[0]}{digits[-1]}')
            val += num
        print(val)
