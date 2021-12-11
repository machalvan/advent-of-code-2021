def flash(grid, flashed, x, y):
    if flashed[y][x]:
        return grid, flashed

    flashed[y][x] = True

    w = len(grid[0])
    h = len(grid)
    for i in range(-1, 1 + 1):
        for j in range(-1, 1 + 1):
            if i == 0 and j == 0:
                continue

            if 0 <= y + j < h and 0 <= x + i < w:
                grid[y + j][x + i] += 1

    for y2 in range(h):
        for x2 in range(w):
            if grid[y2][x2] > 9:
                grid, flashed = flash(grid, flashed, x2, y2)

    grid[y][x] = 0
    return grid, flashed


def part1(lines):
    grid = [[int(char) for char in line] for line in lines]

    res = 0
    for step in range(100):
        w = len(grid[0])
        h = len(grid)
        flashed = [[False for _ in range(w)] for _ in range(h)]
        grid = [[num + 1 for num in row] for row in grid]

        for y in range(h):
            for x in range(w):
                if grid[y][x] > 9:
                    grid, flashed = flash(grid, flashed, x, y)

        res += sum(sum(f) for f in flashed)

    return res


def part2(lines):
    grid = [[int(char) for char in line] for line in lines]

    for step in range(1000):
        w = len(grid[0])
        h = len(grid)
        flashed = [[False for _ in range(w)] for _ in range(h)]
        grid = [[num + 1 for num in row] for row in grid]

        for y in range(h):
            for x in range(w):
                if grid[y][x] > 9:
                    grid, flashed = flash(grid, flashed, x, y)

        if all(all(f) for f in flashed):
            return step + 1


if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt')]
    print(part1(lines))
    print(part2(lines))
