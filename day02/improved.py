from utils import *


def part1(input):
    hor = depth = 0
    words = [line.split() for line in input]
    words = [(a, int(b)) for a, b in words]

    for dir, units in words:
        match dir:
            case 'forward':
                hor += units
            case 'down':
                depth += units
            case 'up':
                depth -= units

    return hor * depth


def part2(input):
    hor = depth = aim = 0
    words = [line.split() for line in input]
    words = [(a, int(b)) for a, b in words]

    for dir, units in words:
        match dir:
            case 'forward':
                hor += units
                depth += aim * units
            case 'down':
                aim += units
            case 'up':
                aim -= units

    return hor * depth


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
