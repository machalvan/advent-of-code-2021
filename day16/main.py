from math import prod

res = 0


def get_packet(bits):
    global res

    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    res += version

    packets = []
    packet = ''
    i = 6
    if type_id == 4:
        while bits[i] == '1':
            i += 1
            packet += bits[i:i + 4]
            i += 4

        i += 1
        packet += bits[i:i + 4]
        packet = int(packet, 2)
        packets.append(packet)

        remaining = bits[i + 4:]
    else:
        if bits[i] == '0':
            i += 1
            len_of_sub_packets = int(bits[i:i + 15], 2)
            i += 15

            remaining = bits[i:i + len_of_sub_packets]
            while len(remaining) > 0:
                packet, remaining = get_packet(remaining)
                packets.append(packet)

            remaining = bits[i + len_of_sub_packets:]
        else:
            i += 1
            num_of_sub_packets = int(bits[i:i + 11], 2)
            i += 11

            remaining = bits[i:]
            while num_of_sub_packets > 0:
                packet, remaining = get_packet(remaining)
                packets.append(packet)
                num_of_sub_packets -= 1

    if type_id == 0:
        packet = sum(packets)
    elif type_id == 1:
        packet = prod(packets)
    elif type_id == 2:
        packet = min(packets)
    elif type_id == 3:
        packet = max(packets)
    elif type_id == 5:
        packet = 1 if packets[0] > packets[1] else 0
    elif type_id == 6:
        packet = 1 if packets[0] < packets[1] else 0
    elif type_id == 7:
        packet = 1 if packets[0] == packets[1] else 0

    return packet, remaining


def part1(input):
    global res

    bits = bin(int(input, 16))[2:].zfill(4)

    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    res += version

    packet = ''
    i = 6
    if type_id == 4:
        while bits[i] == '1':
            i += 1
            packet += bits[i:i + 4]
            i += 4
    else:
        if bits[i] == '0':
            i += 1
            len_of_sub_packets = int(bits[i:i + 15], 2)
            i += 15

            remaining = bits[i:i + len_of_sub_packets]
            while len(remaining) > 0:
                packet, remaining = get_packet(remaining)
        else:
            i += 1
            num_of_sub_packets = int(bits[i:i + 11], 2)
            i += 11

            remaining = bits[i:]
            for _ in range(num_of_sub_packets):
                packet, remaining = get_packet(remaining)

    return res


def part2(input):
    global res

    bits = bin(int(input, 16))[2:].zfill(4)

    type_id = int(bits[3:6], 2)

    packets = []
    packet = ''
    i = 6
    if type_id == 4:
        while bits[i] == '1':
            i += 1
            packet += bits[i:i + 4]
            i += 4

        i += 1
        packet += bits[i:i + 4]
        packet = int(packet, 2)
        packets.append(packet)
    else:
        if bits[i] == '0':
            i += 1
            len_of_sub_packets = int(bits[i:i + 15], 2)
            i += 15

            remaining = bits[i:i + len_of_sub_packets]
            while len(remaining) > 0:
                packet, remaining = get_packet(remaining)
                packets.append(packet)
        else:
            i += 1
            num_of_sub_packets = int(bits[i:i + 11], 2)
            i += 11

            remaining = bits[i:]
            for _ in range(num_of_sub_packets):
                packet, remaining = get_packet(remaining)
                packets.append(packet)

    if type_id == 0:
        return sum(packets)
    elif type_id == 1:
        return prod(packets)
    elif type_id == 2:
        return min(packets)
    elif type_id == 3:
        return max(packets)
    elif type_id == 5:
        return 1 if packets[0] > packets[1] else 0
    elif type_id == 6:
        return 1 if packets[0] < packets[1] else 0
    elif type_id == 7:
        return 1 if packets[0] == packets[1] else 0


if __name__ == '__main__':
    input = open('input.txt').read().strip()
    print(part1(input))
    print(part2(input))
