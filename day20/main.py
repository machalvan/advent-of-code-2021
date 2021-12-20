def get_enhancement(x, y, input):
    enhanced = ''

    for y2 in [y-1, y, y+1]:
        for x2 in [x-1, x, x+1]:
            if 0 <= x2 < len(input[0]) and 0 <= y2 < len(input):
                enhanced += input[y2][x2]

    return enhanced


def add_dark_borders(input):
    width = len(input[0]) + 2
    return [['.'] * width, *[['.'] + line + ['.'] for line in input], ['.'] * width]


def crop_middle(input, w, h):
    middle_x = int(len(input[0]) / 2)
    middle_y = int(len(input) / 2)
    min_x, max_x = middle_x - (w // 2), middle_x + (w // 2)
    min_y, max_y = middle_y - (h // 2), middle_y + (h // 2)

    new_input = []
    for y, line in enumerate(input):
        new_row = []
        for x, char in enumerate(line):
            if min_x <= x <= max_x and min_y <= y <= max_y:
                new_row.append(char)

        if len(new_row) > 0:
            new_input.append(new_row)

    return new_input


def part1(input):
    blocks = [block.split('\n') for block in input.split('\n\n')]
    alg, input = blocks[0][0], blocks[1]
    input = [list(line) for line in input]
    w, h = len(input[0]), len(input)
    i = 2

    for _ in range(i * 2):
        input = add_dark_borders(input)

    for _ in range(i):
        new_input = []

        for y, line in enumerate(input):
            new_row = []

            for x, char in enumerate(line):
                enhanced = get_enhancement(x, y, input)
                binary = enhanced.replace('#', '1').replace('.', '0')
                decimal = int(binary, 2)
                new_row.append(alg[decimal])

            new_input.append(new_row)
        input = new_input

    input = crop_middle(input, w + i * 2, h + i * 2)

    return sum([bool(char == '#') for line in input for char in line])


def part2(input):
    blocks = [block.split('\n') for block in input.split('\n\n')]
    alg, input = blocks[0][0], blocks[1]
    input = [list(line) for line in input]

    w, h = len(input[0]), len(input)
    i = 50

    for _ in range(i * 2):
        input = add_dark_borders(input)

    for _ in range(i):
        new_input = []

        for y, line in enumerate(input):
            new_row = []

            for x, char in enumerate(line):
                enhanced = get_enhancement(x, y, input)
                binary = enhanced.replace('#', '1').replace('.', '0')
                decimal = int(binary, 2)
                new_row.append(alg[decimal])

            new_input.append(new_row)
        input = new_input

    for line in input:
        print(line)

    input = crop_middle(input, w + i * 2, h + i * 2)

    return sum([bool(char == '#') for line in input for char in line])


if __name__ == '__main__':
    input = open('input.txt').read().strip()
    print(part1(input))
    print(part2(input))
