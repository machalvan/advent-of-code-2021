from math import prod


def part1(lines):
    matrix = [[int(num) for num in line] for line in lines]

    res = 0
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if i - 1 >= 0 and num >= matrix[i - 1][j]:
                continue
            if j - 1 >= 0 and num >= matrix[i][j - 1]:
                continue
            if i + 1 < len(matrix) and num >= matrix[i + 1][j]:
                continue
            if j + 1 < len(row) and num >= matrix[i][j + 1]:
                continue

            res += num + 1

    return res


def part2(lines):
    matrix = [[int(num) for num in line] for line in lines]

    sizes = []
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if i - 1 >= 0 and num >= matrix[i - 1][j]:
                continue
            if j - 1 >= 0 and num >= matrix[i][j - 1]:
                continue
            if i + 1 < len(matrix) and num >= matrix[i + 1][j]:
                continue
            if j + 1 < len(row) and num >= matrix[i][j + 1]:
                continue

            nums = basin(j, i, matrix, [])
            sizes.append(len(nums))

    return prod(sorted(sizes)[-3:])


def basin(x, y, matrix, nums):
    num = matrix[y][x]

    if (x, y) in nums:
        return nums

    if y - 1 >= 0 and num < matrix[y - 1][x] < 9:
        nums = basin(x, y - 1, matrix, nums)
    if x - 1 >= 0 and num < matrix[y][x - 1] < 9:
        nums = basin(x - 1, y, matrix, nums)
    if y + 1 < len(matrix) and num < matrix[y + 1][x] < 9:
        nums = basin(x, y + 1, matrix, nums)
    if x + 1 < len(matrix[0]) and num < matrix[y][x + 1] < 9:
        nums = basin(x + 1, y, matrix, nums)

    nums.append((x, y))
    return nums


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
