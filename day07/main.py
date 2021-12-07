def part1(lines):
    nums = [int(num) for num in lines[0].split(',')]

    res = None
    for i in range(max(nums)):
        fuel = sum([abs(num - i) for num in nums])
        res = fuel if res is None or res > fuel else res

    return res


def part2(lines):
    nums = [int(num) for num in lines[0].split(',')]

    res = None
    for i in range(max(nums)):
        fuel = sum([int((abs(num - i) * (abs(num - i) + 1)) / 2) for num in nums])
        res = fuel if res is None or res > fuel else res

    return res


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
