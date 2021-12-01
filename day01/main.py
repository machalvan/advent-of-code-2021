from utils import *


def part1(input):
    input = int_list(input)
    res = 0

    for i in range(len(input) - 1):
        if input[i + 1] > input[i]:
            res += 1

    return res


def part2(input):
    input = int_list(input)
    res = 0

    for i in range(len(input) - 3):
        if input[i + 3] + input[i + 2] + input[i + 1] > input[i + 2] + input[i + 1] + input[i]:
            res += 1

    return res


if __name__ == '__main__':
    with open('input.txt') as f:
        file_str = f.read()
        file = file_str.strip().split('\n')

    print(part1(list(file)))
    print(part2(list(file)))
