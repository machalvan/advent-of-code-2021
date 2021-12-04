from utils import int_list, transpose


def part1(lines):
    nums, *board = lines
    nums = [int(num) for num in nums.split(',')]
    boards = [[[
        int(cell) for cell in row.split()
    ] for row in board.split('\n')
    ] for board in '\n'.join(board).strip().split('\n\n')
    ]

    for num in nums:
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, cell in enumerate(row):
                    if num == cell:
                        boards[i][j][k] = True

                        row_bingo = any([all([cell is True for cell in row]) for row in board])
                        col_bingo = any([all([cell is True for cell in col]) for col in board])

                        if row_bingo or col_bingo:
                            unmarked = sum([sum([cell for cell in row if cell is not True]) for row in board])
                            return num * unmarked


def part2(lines):
    nums, *board = lines
    nums = [int(num) for num in nums.split(',')]
    boards = [[[
        int(cell) for cell in row.split()
    ] for row in board.split('\n')
    ] for board in '\n'.join(board).strip().split('\n\n')
    ]

    winners = []
    for num in nums:
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, cell in enumerate(row):
                    if num == cell:
                        boards[i][j][k] = True

                        row_bingo = any([all([cell is True for cell in row]) for row in board])
                        col_bingo = any([all([cell is True for cell in col]) for col in board])

                        if (row_bingo or col_bingo) and i not in winners:
                            winners.append(i)

                        if len(winners) == len(boards):
                            unmarked = sum([sum([cell for cell in row if cell is not True]) for row in board])
                            return num * unmarked


if __name__ == '__main__':
    # with open('input.txt') as f:
    #     numbers, *boards = f.read().rstrip().split('\n\n')
    # print(boards)
    #
    # numbers = [int(num) for num in numbers.split(',')]
    #
    # boards = [[line.split() for line in board.split('\n')] for board in boards]
    #
    # print(boards)

    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
