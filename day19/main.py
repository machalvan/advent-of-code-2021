class Scanner:
    rotations = [
        lambda x, y, z: ((-y, x, z), (-x, -y, z), (y, -x, z)),
        lambda x, y, z: ((z, y, -x), (-x, y, z), (-z, y, x)),
        lambda x, y, z: ((x, -z, y), (x, -y, -z), (x, z, -y)),
    ]

    def __init__(self, beacons):
        self.beacon_set = frozenset(beacons)
        self.rotations = self.get_rotations()
        self.pos = (0, 0, 0)

    def get_rotations(self):
        clouds = {self.beacon_set}

        for rotate in Scanner.rotations:
            temp_clouds = set()

            for beacons in clouds:
                rotated = set(zip(*(rotate(*beacon) for beacon in beacons)))
                temp_clouds |= rotated
            clouds |= temp_clouds

        return clouds


def match(anchor, scanner):
    for rotation in scanner.rotations:
        for x1, y1, z1 in anchor.beacon_set:
            for x2, y2, z2 in rotation:
                dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
                cloud = set((x + dx, y + dy, z + dz) for x, y, z in rotation)
                if len(anchor.beacon_set & cloud) >= 12:
                    return cloud, (dx, dy, dz)

    return None, None


def manhattan_dist(a, b):
    return sum([abs(x - y) for x, y in zip(a, b)])


def part1(input):
    all_beacons = [[tuple(
        int(num)
        for num in line.split(','))
        for line in block.split('\n')[1:]]
        for block in input.split('\n\n')]

    scanners = [Scanner(beacons) for beacons in all_beacons]
    beacons = {*all_beacons[0]}
    anchors, to_match = scanners[:1], scanners[1:]

    while anchors:
        anchor = anchors.pop()
        temp = []

        for scanner in to_match:
            abs_beacons, pos = match(anchor, scanner)

            if abs_beacons is not None:
                beacons |= abs_beacons
                scanner.beacon_set = abs_beacons
                anchors.append(scanner)
                scanner.pos = pos
            else:
                temp.append(scanner)
        to_match = temp

    return len(beacons)


def part2(input):
    all_beacons = [[tuple(
        int(num)
        for num in line.split(','))
        for line in block.split('\n')[1:]]
        for block in input.split('\n\n')]

    scanners = [Scanner(beacons) for beacons in all_beacons]
    beacons = {*all_beacons[0]}
    anchors, to_match = scanners[:1], scanners[1:]

    while anchors:
        anchor = anchors.pop()
        temp = []

        for scanner in to_match:
            abs_beacons, pos = match(anchor, scanner)

            if abs_beacons is not None:
                beacons |= abs_beacons
                scanner.beacon_set = abs_beacons
                anchors.append(scanner)
                scanner.pos = pos
            else:
                temp.append(scanner)
        to_match = temp

    pos = [scanner.pos for scanner in scanners]

    return max([manhattan_dist(pos[i], pos[j]) for i in range(len(pos)) for j in range(i + 1, len(pos))])


if __name__ == '__main__':
    input = open('input.txt').read().strip()
    print(part1(input))
    print(part2(input))
