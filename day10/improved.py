def part1(lines):
    res = 0
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}

    for line in lines:
        stack = []

        for char in line:
            popped = stack.append(char) if char in pairs.keys() else stack.pop()
            res += points[char] if popped and char != pairs[popped] else 0

    return res


def part2(lines):
    scores = []
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    points = {')': 1, ']': 2, '}': 3, '>': 4}

    for line in lines:
        stack = []

        for char in line:
            stack.append(char) if char in pairs.keys() else stack.pop()

        score = sum([points[pairs[char]] * 5 ** i for i, char in enumerate(stack)])
        scores.append(score)

    return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
