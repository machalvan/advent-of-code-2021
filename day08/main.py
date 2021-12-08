def part1(lines):
    return sum(sum(len(word) in [2, 3, 4, 7] for word in line.split('|')[1].split()) for line in lines)


def part2(lines):
    res = 0

    for line in lines:
        input, output = line.split('|')
        input = input.split()
        output = output.split()

        display = {}
        segment_dict = {}
        mapping = {}
        for i, word in enumerate(input):
            match len(word):
                case 2:
                    display[1] = word
                case 4:
                    display[4] = word
                case 3:
                    display[7] = word
                case 7:
                    display[8] = word

        for i, word in enumerate(input):
            for char in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
                if char in word:
                    mapping[char] = mapping.get(char, 0) + 1

        segment_dict[0] = [char for char in display[7] if char not in display[1]][0]
        segment_dict[6] = [k for k, v in mapping.items() if v == 9][0]
        segment_dict[1] = [k for k, v in mapping.items() if v == 6][0]
        segment_dict[4] = [k for k, v in mapping.items() if v == 4][0]
        segment_dict[3] = [k for k, v in mapping.items() if v == 8 and k in display[1]][0]
        segment_dict[2] = [k for k, v in mapping.items() if v == 7 and k in display[4]][0]
        segment_dict[5] = [a for a in ['a', 'b', 'c', 'd', 'e', 'f', 'g'] if a not in segment_dict.values()][0]

        inv_segments = {v: k for k, v in segment_dict.items()}

        digits = ''
        for word in output:
            segments = sorted([inv_segments[char] for char in word])

            match segments:
                case [3, 6]:
                    digits += '1'
                case [0, 2, 3, 4, 5]:
                    digits += '2'
                case [0, 2, 3, 5, 6]:
                    digits += '3'
                case [1, 2, 3, 6]:
                    digits += '4'
                case [0, 1, 2, 5, 6]:
                    digits += '5'
                case [0, 1, 2, 4, 5, 6]:
                    digits += '6'
                case [0, 3, 6]:
                    digits += '7'
                case [0, 1, 2, 3, 4, 5, 6]:
                    digits += '8'
                case [0, 1, 2, 3, 5, 6]:
                    digits += '9'
                case [0, 1, 3, 4, 5, 6]:
                    digits += '0'

        res += int(digits)

    return res


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
