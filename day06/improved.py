from collections import deque


def part1(lines):
    nums = lines[0].split(',')
    nums = deque([nums.count(str(num)) for num in range(9)])

    for _ in range(80):
        nums.rotate(-1)
        nums[6] += nums[8]

    return sum(nums)


def part2(lines):
    nums = lines[0].split(',')
    nums = deque([nums.count(str(num)) for num in range(9)])

    for _ in range(256):
        nums.rotate(-1)
        nums[6] += nums[8]

    return sum(nums)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
