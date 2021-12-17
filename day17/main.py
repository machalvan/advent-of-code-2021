import re


def target_in_trajectory(xv, yv, target_area):
    x, y = 0, 0
    x_min, x_max, y_min, y_max = target_area
    highest = y

    for i in range(1000):
        x += xv
        y += yv
        xv = xv - 1 if xv > 0 else xv + 1 if xv < 0 else xv
        yv -= 1
        highest = y if y > highest else highest

        if x > x_max or y < y_min:
            break
        elif x >= x_min and y <= y_max:
            return highest

    return None


def part1(input):
    target_area = [int(num) for num in re.findall(r'-?\d+', input)]

    res = 0
    for vy in range(-500, 500):
        for vx in range(500):
            highest = target_in_trajectory(vx, vy, target_area)

            if highest is not None:
                res = highest if highest > res else res

    return res


def part2(input):
    target_area = [int(num) for num in re.findall(r'-?\d+', input)]

    res = 0
    for vy in range(-500, 500):
        for vx in range(500):
            if target_in_trajectory(vx, vy, target_area) is not None:
                res += 1

    return res


if __name__ == '__main__':
    input = open('input.txt').read().strip()
    print(part1(input))
    print(part2(input))
