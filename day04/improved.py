def part1(lines):
    nums, *boards = lines.split('\n\n')
    nums = [int(num) for num in nums.split(',')]
    boards = [[[
        int(cell)
        for cell in row.split()]
        for row in board.split('\n')]
        for board in boards]

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
    nums, *boards = lines.split('\n\n')
    nums = [int(num) for num in nums.split(',')]
    boards = [[[
        int(cell)
        for cell in row.split()]
        for row in board.split('\n')]
        for board in boards]

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
    with open('input.txt') as f:
        lines = f.read()

    print(part1(lines))
    print(part2(lines))
