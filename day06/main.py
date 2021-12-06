def part1(lines):
    numbers = {key: 0 for key in range(0, 9)}

    for num in [int(x) for x in lines[0].split(',')]:
        numbers[num] += 1

    for i in range(80):
        temp = numbers[0]

        numbers[0] = numbers[1]
        numbers[1] = numbers[2]
        numbers[2] = numbers[3]
        numbers[3] = numbers[4]
        numbers[4] = numbers[5]
        numbers[5] = numbers[6]
        numbers[6] = temp + numbers[7]
        numbers[7] = numbers[8]
        numbers[8] = temp

    return sum(numbers.values())


def part2(lines):
    numbers = {key: 0 for key in range(0, 9)}

    for num in [int(x) for x in lines[0].split(',')]:
        numbers[num] += 1

    for i in range(256):
        temp = numbers[0]

        numbers[0] = numbers[1]
        numbers[1] = numbers[2]
        numbers[2] = numbers[3]
        numbers[3] = numbers[4]
        numbers[4] = numbers[5]
        numbers[5] = numbers[6]
        numbers[6] = temp + numbers[7]
        numbers[7] = numbers[8]
        numbers[8] = temp

    return sum(numbers.values())


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
