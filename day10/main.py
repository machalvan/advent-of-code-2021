def part1(lines):
    res = 0

    for line in lines:
        stack = []
        prev_res = res

        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif char in [')', ']', '}', '>']:
                popped = stack.pop()

                match char:
                    case ')':
                        if popped != '(':
                            res += 3
                    case ']':
                        if popped != '[':
                            res += 57
                    case '}':
                        if popped != '{':
                            res += 1197
                    case '>':
                        if popped != '<':
                            res += 25137

                if res != prev_res:
                    break

    return res


def part2(lines):
    res = 0
    points = []

    for line in lines:
        ans = 0
        stack = []
        prev_res = res
        for char in line:
            if char in ['(', '[', '{', '<']:
                stack.append(char)
            elif char in [')', ']', '}', '>']:
                popped = stack.pop()

                match char:
                    case ')':
                        if popped != '(':
                            res += 3
                    case ']':
                        if popped != '[':
                            res += 57
                    case '}':
                        if popped != '{':
                            res += 1197
                    case '>':
                        if popped != '<':
                            res += 25137

            if res != prev_res:
                break
        if res != prev_res:
            continue

        for char in stack[::-1]:
            ans *= 5

            if char == '(':
                ans += 1
            elif char == '[':
                ans += 2
            elif char == '{':
                ans += 3
            elif char == '<':
                ans += 4
        points.append(ans)

    points = sorted(points)
    return points[len(points) // 2]


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
