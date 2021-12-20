from math import floor, ceil

REDUCE = True


class Pair:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.memo_left = 0
        self.memo_right = 0
        self.parent = None

        if isinstance(self.left, Pair):
            self.left.parent = self

        if isinstance(self.right, Pair):
            self.right.parent = self

    def get_rightmost_pair(self):
        return self.right.get_rightmost_pair() if isinstance(self.right, Pair) else self

    def get_leftmost_pair(self):
        return self.left.get_leftmost_pair() if isinstance(self.left, Pair) else self

    def increment_right_neighbour_pair(self, amount):
        if self.parent is None:
            return

        if self.parent.right != self:
            if isinstance(self.parent.right, int):
                self.parent.right += amount
            else:
                leftmost = self.parent.right.get_leftmost_pair()
                leftmost.left += amount
        else:
            self.parent.increment_right_neighbour_pair(amount)

    def increment_left_neighbour_pair(self, amount):
        if self.parent is None:
            return None

        if self.parent.left != self:
            if isinstance(self.parent.left, int):
                self.parent.left += amount
            else:
                rightmost = self.parent.left.get_rightmost_pair()
                rightmost.right += amount
        else:
            self.parent.increment_left_neighbour_pair(amount)

    def explode(self):
        self.increment_left_neighbour_pair(self.left)
        self.increment_right_neighbour_pair(self.right)

        if self.parent.left == self:
            self.parent.left = 0
        else:
            self.parent.right = 0


def parse(line):
    arr, stack = [], []
    element, num = '', ''

    for i, char in enumerate(line[1:-1]):
        if char.isnumeric():
            num += char
            continue

        if char == '[':
            if len(stack) == 0:
                element = ''
            stack.append(char)

        if num != '':
            element += num + char
            if len(stack) == 0:
                arr.append(int(num))
            num = ''
        else:
            element += char

        if char == ']':
            stack.pop()
            if len(stack) == 0:
                inner = parse(element)
                arr.append(inner)
                element = ''

    if num != '':
        element += num
        if len(stack) == 0:
            arr.append(int(num))

    return arr


def parse_pair(arr):
    if isinstance(arr, int):
        return arr

    left = parse_pair(arr[0])
    right = parse_pair(arr[1])

    return Pair(left, right)


def check_for_explode(arr, nested=0):
    global REDUCE

    if isinstance(arr, int):
        return False

    if nested >= 4 and isinstance(arr.left, int) and isinstance(arr.right, int):
        arr.explode()
        REDUCE = True
        return True

    check_for_explode(arr.left, nested + 1)
    check_for_explode(arr.right, nested + 1)


def check_for_split(arr):
    global REDUCE

    if isinstance(arr.left, int):
        if len(str(arr.left)) > 1:
            arr.left = Pair(floor(arr.left / 2), ceil(arr.left / 2))
            arr.left.parent = arr
            REDUCE = True
    else:
        check_for_split(arr.left)

    if REDUCE:
        return

    if isinstance(arr.right, int):
        if len(str(arr.right)) > 1:
            arr.right = Pair(floor(arr.right / 2), ceil(arr.right / 2))
            arr.right.parent = arr
            REDUCE = True
    else:
        check_for_split(arr.right)


def magnitude(arr):
    mag = 3 * (arr.left if isinstance(arr.left, int) else magnitude(arr.left))
    mag += 2 * (arr.right if isinstance(arr.right, int) else magnitude(arr.right))
    return mag


def part1(input):
    global REDUCE

    lines = input.split('\n')

    arr = parse_pair(parse(lines[0]))
    for i in range(1, len(lines)):
        other = parse_pair(parse(lines[i]))
        arr = Pair(arr, other)

        REDUCE = True
        while REDUCE:
            REDUCE = False
            check_for_explode(arr)

            if REDUCE:
                continue

            check_for_split(arr)

    return magnitude(arr)


def part2(input):
    global REDUCE

    lines = input.split('\n')

    arr = parse_pair(parse(lines[0]))
    for i in range(1, len(lines)):
        other = parse_pair(parse(lines[i]))
        arr = Pair(arr, other)

        REDUCE = True
        while REDUCE:
            REDUCE = False
            check_for_explode(arr)

            if REDUCE:
                continue

            check_for_split(arr)

    highest = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j:
                continue

            pair1 = parse_pair(parse(lines[i]))
            pair2 = parse_pair(parse(lines[j]))

            arr = Pair(pair1, pair2)

            REDUCE = True
            while REDUCE:
                REDUCE = False
                check_for_explode(arr)

                if REDUCE:
                    continue

                check_for_split(arr)

            mag = magnitude(arr)

            if mag > highest:
                highest = mag

    return highest


if __name__ == '__main__':
    input = open('input.txt').read().strip()
    print(part1(input))
    print(part2(input))
