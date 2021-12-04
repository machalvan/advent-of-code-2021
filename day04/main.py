from utils import int_list, transpose


def part1(lines):
    nums = int_list(lines[0].split(','))

    boards = []
    board = []
    for line in lines[2:]:
        if line == '':
            boards.append(board)
            board = []
            continue

        row = [(cell, False) for cell in int_list(line.split())]
        board.append(row)

    for num in nums:
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, cell in enumerate(row):
                    if num == cell[0]:
                        boards[i][j][k] = (num, True)

            rows = [[cell[1] for cell in row] for row in board]
            row_bingo = any([all([cell for cell in row]) for row in rows])
            cols = [[cell[1] for cell in row] for row in transpose(board)]
            col_bingo = any([all([cell for cell in col]) for col in cols])

            if row_bingo or col_bingo:
                unmarked = sum([sum([cell[0] for cell in row if not cell[1]]) for row in board])
                return num * unmarked


def part2(lines):
    nums = int_list(lines[0].split(','))

    boards = []
    board = []
    for line in lines[2:]:
        if line == '':
            boards.append(board)
            board = []
            continue

        row = [(cell, False) for cell in int_list(line.split())]
        board.append(row)

    winners = []
    for num in nums:
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, cell in enumerate(row):
                    if num == cell[0]:
                        boards[i][j][k] = (num, True)

            rows = [[cell[1] for cell in row] for row in board]
            row_bingo = any([all([cell for cell in row]) for row in rows])
            cols = [[cell[1] for cell in row] for row in transpose(board)]
            col_bingo = any([all([cell for cell in col]) for col in cols])

            if (row_bingo or col_bingo) and i not in winners:
                winners.append(i)

            if len(winners) == len(boards):
                unmarked = sum([sum([cell[0] for cell in row if not cell[1]]) for row in board])
                return num * unmarked


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.strip() for line in f]

    print(part1(lines))
    print(part2(lines))
