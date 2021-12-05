def part1(lines):
    matrix = {}

    for line in lines:
        x1, y1, x2, y2 = [int(num) for num in line.replace('->', ',').split(',')]

        for i in range(max(abs(x1 - x2), abs(y1 - y2)) + 1):
            if x1 != x2 and y1 != y2:
                continue

            x = x1 + (i if x1 < x2 else -i if x1 > x2 else 0)
            y = y1 + (i if y1 < y2 else -i if y1 > y2 else 0)
            matrix[(x, y)] = matrix.get((x, y), 0) + 1

    return sum(cell >= 2 for cell in matrix.values())


def part2(lines):
    matrix = {}

    for line in lines:
        x1, y1, x2, y2 = [int(num) for num in line.replace('->', ',').split(',')]

        for i in range(max(abs(x1 - x2), abs(y1 - y2)) + 1):
            x = x1 + (i if x1 < x2 else -i if x1 > x2 else 0)
            y = y1 + (i if y1 < y2 else -i if y1 > y2 else 0)
            matrix[(x, y)] = matrix.get((x, y), 0) + 1

    return sum(cell >= 2 for cell in matrix.values())


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
