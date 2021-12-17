from math import prod


def get_packet(bits, version_sum=0):
    version, bits = int(bits[:3], 2), bits[3:]
    type_id, bits = int(bits[:3], 2), bits[3:]

    version_sum += version

    sub_packets = []
    if type_id == 4:
        prefix, bits = bits[0], bits[1:]

        packet = ''
        while prefix == '1':
            group, bits = bits[:4], bits[4:]
            packet += group
            prefix, bits = bits[0], bits[1:]

        group, bits = bits[:4], bits[4:]
        packet += group
    else:
        len_type_id, bits = bits[0], bits[1:]

        if len_type_id == '0':
            len_of_sub_packets, bits = int(bits[:15], 2), bits[15:]
            sub_packet_bits, bits = bits[:len_of_sub_packets], bits[len_of_sub_packets:]

            while len(sub_packet_bits) > 0:
                version_sum, packet, sub_packet_bits = get_packet(sub_packet_bits, version_sum)
                sub_packets.append(packet)
        else:
            num_of_sub_packets, bits = int(bits[:11], 2), bits[11:]

            for _ in range(num_of_sub_packets):
                version_sum, packet, bits = get_packet(bits, version_sum)
                sub_packets.append(packet)
    func = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        4: lambda x: int(x, 2),
        5: lambda x: 1 if x[0] > x[1] else 0,
        6: lambda x: 1 if x[0] < x[1] else 0,
        7: lambda x: 1 if x[0] == x[1] else 0,
    }[type_id]

    packet_value = func(packet) if type_id == 4 else func(sub_packets)

    return version_sum, packet_value, bits


def part1(input):
    bits = bin(int(input, 16))[2:].zfill(len(input) * 4)
    return get_packet(bits)[0]


def part2(input):
    bits = bin(int(input, 16))[2:].zfill(len(input) * 4)
    return get_packet(bits)[1]


if __name__ == '__main__':
    input = open('input.txt').read().strip()
    print(part1(input))
    print(part2(input))
