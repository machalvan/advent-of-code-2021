from utils import *


def part1(input):
    hor = depth = 0

    for line in input:
        dir, units = line.split()
        units = int(units)

        if dir == 'forward':
            hor += units
        elif dir == 'down':
            depth += units
        elif dir == 'up':
            depth -= units

    return hor * depth


def part2(input):
    hor = depth = aim = 0

    for line in input:
        dir, units = line.split()
        units = int(units)

        if dir == 'forward':
            hor += units
            depth += aim * units
        elif dir == 'down':
            aim += units
        elif dir == 'up':
            aim -= units

    return hor * depth


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
