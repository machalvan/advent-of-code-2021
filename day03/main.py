def part1(lines):
    gamma = ''

    for index, _ in enumerate(lines[0]):
        bits = [int(line[index]) for line in lines]
        gamma += str(0 if bits.count(0) > bits.count(1) else 1)

    epsilon = ''.join([str(0 if int(bit) == 1 else 1) for bit in gamma])

    return int(gamma, 2) * int(epsilon, 2)


def part2(lines):
    oxygen = lines

    for index, _ in enumerate(lines[0]):
        bits = [int(line[index]) for line in oxygen]
        common = 0 if bits.count(0) > bits.count(1) else 1
        oxygen = [line for line in oxygen if int(line[index]) == common]

        if len(oxygen) == 1:
            oxygen = oxygen[0]
            break

    co2 = lines
    for index, _ in enumerate(lines[0]):
        bits = [int(line[index]) for line in co2]
        common = 1 if bits.count(0) > bits.count(1) else 0
        co2 = [line for line in co2 if int(line[index]) == common]

        if len(co2) == 1:
            co2 = co2[0]
            break

    return int(oxygen, 2) * int(co2, 2)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
