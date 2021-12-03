def part1(lines):
    gamma = ''.join([
        '0' if bits.count('0') > bits.count('1') else '1'
        for bits in map(list, zip(*lines))
    ])
    epsilon = ''.join(['0' if bit == '1' else '1' for bit in gamma])

    return int(gamma, 2) * int(epsilon, 2)


def part2(lines):
    oxygen = co2 = lines

    index = 0
    while len(oxygen) > 1:
        bits = [line[index] for line in oxygen]
        common = '0' if bits.count('0') > bits.count('1') else '1'
        oxygen = [line for line in oxygen if line[index] == common]
        index += 1

    index = 0
    while len(co2) > 1:
        bits = [line[index] for line in co2]
        least_common = '1' if bits.count('0') > bits.count('1') else '0'
        co2 = [line for line in co2 if line[index] == least_common]
        index += 1

    return int(oxygen[0], 2) * int(co2[0], 2)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
