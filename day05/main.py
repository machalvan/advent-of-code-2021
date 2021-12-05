def part1(lines):
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    for row in lines:
        point1, point2 = [[int(x) for x in point.split(',')] for point in row.split(' -> ')]

        if point1[0] == point2[0]:
            if point1[1] < point2[1]:
                for i in range(point1[1], point2[1] + 1):
                    matrix[point1[0]][i] += 1
            else:
                for i in range(point2[1], point1[1] + 1):
                    matrix[point1[0]][i] += 1
        elif point1[1] == point2[1]:
            if point1[0] < point2[0]:
                for i in range(point1[0], point2[0] + 1):
                    matrix[i][point1[1]] += 1
            else:
                for i in range(point2[0], point1[0] + 1):
                    matrix[i][point1[1]] += 1

    res = 0
    for row in matrix:
        for cell in row:
            if cell >= 2:
                res += 1

    return res


def part2(lines):
    matrix = [[0 for _ in range(1000)] for _ in range(1000)]

    for row in lines:
        point1, point2 = [[int(x) for x in point.split(',')] for point in row.split(' -> ')]

        if point1[0] == point2[0]:
            if point1[1] < point2[1]:
                for i in range(point1[1], point2[1] + 1):
                    matrix[point1[0]][i] += 1
            else:
                for i in range(point2[1], point1[1] + 1):
                    matrix[point1[0]][i] += 1
        elif point1[1] == point2[1]:
            if point1[0] < point2[0]:
                for i in range(point1[0], point2[0] + 1):
                    matrix[i][point1[1]] += 1
            else:
                for i in range(point2[0], point1[0] + 1):
                    matrix[i][point1[1]] += 1
        else:
            if point1[0] < point2[0]:
                if point1[1] < point2[1]:
                    for i in range(abs(point1[0] - point2[0]) + 1):
                        matrix[point1[0] + i][point1[1] + i] += 1
                else:
                    for i in range(abs(point1[0] - point2[0]) + 1):
                        matrix[point1[0] + i][point1[1] - i] += 1
            else:
                if point1[1] < point2[1]:
                    for i in range(abs(point1[0] - point2[0]) + 1):
                        matrix[point1[0] - i][point1[1] + i] += 1
                else:
                    for i in range(abs(point1[0] - point2[0]) + 1):
                        matrix[point1[0] - i][point1[1] - i] += 1

    res = 0
    for row in matrix:
        for cell in row:
            if cell >= 2:
                res += 1

    return res


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
