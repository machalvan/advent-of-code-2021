def int_list(str_list):
    return list(map(int, str_list))


def transpose(matrix):
    """Transpose a matrix
    Examples:
        >>> transpose([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    return list(map(list, zip(*matrix)))
