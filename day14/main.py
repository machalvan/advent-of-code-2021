from collections import Counter

memo = {}


def part1(lines):
    template, pairs = '\n'.join(lines).split('\n\n')
    pairs = {k: v for k, v in [pair.split(' -> ') for pair in pairs.split('\n')]}

    res = Counter()
    prev = template[0]
    for char in template[1:]:
        res += get_counter(prev, char, pairs, 10)
        prev = char

    res += Counter(template[-1])
    return Counter(res).most_common(1)[0][1] - Counter(res).most_common()[-1][1]


def part2(lines):
    template, pairs = '\n'.join(lines).split('\n\n')
    pairs = {k: v for k, v in [pair.split(' -> ') for pair in pairs.split('\n')]}

    res = Counter()
    prev = template[0]
    for char in template[1:]:
        res += get_counter(prev, char, pairs, 40)
        prev = char

    res += Counter(template[-1])
    return Counter(res).most_common(1)[0][1] - Counter(res).most_common()[-1][1]


def get_counter(first, last, pairs, steps):
    between = pairs[first + last]

    if steps <= 1:
        return Counter([first, between])

    if (first, between, steps - 1) not in memo:
        memo[(first, between, steps - 1)] = get_counter(first, between, pairs, steps - 1)

    if (between, last, steps - 1) not in memo:
        memo[(between, last, steps - 1)] = get_counter(between, last, pairs, steps - 1)

    return memo[(first, between, steps - 1)] + memo[(between, last, steps - 1)]


if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt')]
    print(part1(lines))
    print(part2(lines))
