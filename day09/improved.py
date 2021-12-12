from math import prod


def part1(lines):
    matrix = [[int(num) for num in line] for line in lines]

    res = 0
    for y, row in enumerate(matrix):
        for x, num in enumerate(row):
            for x2, y2 in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                if 0 <= y2 < len(matrix) and 0 <= x2 < len(row) and matrix[y2][x2] <= num:
                    break
            else:
                res += num + 1

    return res


def part2(lines):
    matrix = [[int(num) for num in line] for line in lines]

    sizes = []
    for y, row in enumerate(matrix):
        for x, num in enumerate(row):
            for x2, y2 in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                if 0 <= y2 < len(matrix) and 0 <= x2 < len(row) and matrix[y2][x2] <= num:
                    break
            else:
                sizes.append(len(basin(x, y, matrix, [])))

    return prod(sorted(sizes)[-3:])


def basin(x, y, matrix, nums):
    if (x, y) in nums:
        return nums

    for x2, y2 in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
        if 0 <= y2 < len(matrix) and 0 <= x2 < len(matrix[0]) and matrix[y][x] < matrix[y2][x2] < 9:
            nums = basin(x2, y2, matrix, nums)

    return nums + [(x, y)]


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
