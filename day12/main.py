def find_paths_part1(graph, start, end, path=None):
    path = [start] if path is None else path + [start]

    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node in path and node.islower():
            continue

        paths.extend(find_paths_part1(graph, node, end, path))

    return paths


def find_paths_part2(graph, start, end, path=None):
    path = [start] if path is None else path + [start]

    if start == end or start == 'end':
        return [path]
    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        twice_used = any([path.count(n) >= 2 for n in path if n.islower()])
        if node in path and node.islower() and twice_used or node == 'start':
            continue

        paths.extend(find_paths_part2(graph, node, end, path))

    return paths


def part1(lines):
    graph = {}

    for line in lines:
        start, end = line.split('-')
        graph[start] = graph.get(start, []) + [end]
        graph[end] = graph.get(end, []) + [start]

    return len(find_paths_part1(graph, 'start', 'end'))


def part2(lines):
    graph = {}

    for line in lines:
        start, end = line.split('-')
        graph[start] = graph.get(start, []) + [end]
        graph[end] = graph.get(end, []) + [start]

    return len(find_paths_part2(graph, 'start', 'end'))


if __name__ == '__main__':
    lines = [line.strip() for line in open('input.txt')]
    print(part1(lines))
    print(part2(lines))
