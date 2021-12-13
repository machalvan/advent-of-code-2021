def part1(lines):
    dots, folds = [block.split('\n') for block in '\n'.join(lines).split('\n\n')]

    paper = {}
    for line in dots:
        dot = tuple([int(num) for num in line.split(',')])
        paper[dot] = True

    for line in folds[:1]:
        dir, value = line.split()[-1].split('=')
        value = int(value)

        folded_paper = {}
        max_x = max(x for (x, y), dot in paper.items() if dot) + 1
        max_y = max(y for (x, y), dot in paper.items() if dot) + 1
        for y in range(max_y):
            for x in range(max_x):
                if dir == 'y':
                    if y < value:
                        folded_paper[(x, y)] = paper.get((x, y)) or paper.get((x, 2 * value - y))
                else:
                    if x < value:
                        folded_paper[(x, y)] = paper.get((x, y)) or paper.get((2 * value - x, y))

        paper = folded_paper

    return sum(v for v in paper.values() if v)


def part2(lines):
    dots, folds = [block.split('\n') for block in '\n'.join(lines).split('\n\n')]

    paper = {}
    for line in dots:
        dot = tuple([int(num) for num in line.split(',')])
        paper[dot] = True

    for line in folds:
        dir, value = line.split()[-1].split('=')
        value = int(value)

        folded_paper = {}
        max_x = max(x for (x, y), dot in paper.items() if dot) + 1
        max_y = max(y for (x, y), dot in paper.items() if dot) + 1
        for y in range(max_y):
            for x in range(max_x):
                if dir == 'y':
                    if y < value:
                        folded_paper[(x, y)] = paper.get((x, y)) or paper.get((x, 2 * value - y))
                else:
                    if x < value:
                        folded_paper[(x, y)] = paper.get((x, y)) or paper.get((2 * value - x, y))

        paper = folded_paper

    max_x = max(x for (x, y), dot in paper.items() if dot) + 1
    max_y = max(y for (x, y), dot in paper.items() if dot) + 1
    return '\n'.join(''.join(['#' if paper.get((x, y)) else '.' for x in range(max_x)]) for y in range(max_y))


if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt')]
    print(part1(lines))
    print(part2(lines))
