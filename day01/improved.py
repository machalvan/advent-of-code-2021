from utils import *


def part1(input):
    return sum([int(b) > int(a) for a, b in zip(input, input[1:])])


def part2(input):
    return sum([int(b) > int(a) for a, b in zip(input, input[3:])])


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
