from heapq import heappush, heappop


def part1(lines):
    matrix = [[int(cell) for cell in line] for line in lines]

    w, h = len(matrix[0]), len(matrix)
    queue = [(0, 0, 0)]
    visited = set()
    while queue:
        risk, x, y = heappop(queue)

        if x == w - 1 and y == h - 1:
            return risk

        for x2, y2 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (x2, y2) not in visited and 0 <= x2 < w and 0 <= y2 < h:
                heappush(queue, (risk + matrix[y2][x2], x2, y2))
                visited.add((x2, y2))


def part2(lines):
    matrix = [[int(cell) for cell in line] for line in lines]
    matrix = [line * 5 for line in matrix * 5]

    w, h = len(matrix[0]), len(matrix)
    for y in range(h):
        for x in range(w):
            matrix[y][x] += y * 5 // h + x * 5 // w
            while matrix[y][x] > 9:
                matrix[y][x] -= 9

    queue = [(0, 0, 0)]
    visited = set()
    while queue:
        risk, x, y = heappop(queue)

        if x == w - 1 and y == h - 1:
            return risk

        for x2, y2 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (x2, y2) not in visited and 0 <= x2 < w and 0 <= y2 < h:
                heappush(queue, (risk + matrix[y2][x2], x2, y2))
                visited.add((x2, y2))


if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt')]
    print(part1(lines))
    print(part2(lines))
