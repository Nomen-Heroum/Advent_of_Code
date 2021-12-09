import src  # My utility functions
import numpy as np
from copy import copy

INPUT = src.read(split='\n\n')
ORDER = [int(n) for n in INPUT[0].split(',')]
BOARDS = [np.genfromtxt(board.splitlines(), int) for board in INPUT[1:]]


def play_bingo(order, boards, size=5, version=1):
    rows_columns = [[set(board[i]) for i in range(size)] + [set(board[:, i]) for i in range(size)]
                    for board in boards]
    for number in order:
        new_boards = copy(rows_columns)
        for board in rows_columns:
            for row_col in board:
                row_col -= {number}
                if not row_col:
                    if version == 2 and len(rows_columns) > 1:
                        new_boards.remove(board)
                        break
                    else:
                        score = number * sum(set().union(*board) - {number})
                        return score
        rows_columns = new_boards


def main(order=None, boards=None):
    order = order or ORDER
    boards = boards or BOARDS

    print("Part One:")
    ans1 = play_bingo(order, boards)  # 82440
    print(f"The winning board has a final score of {ans1}.")

    print("\nPart Two:")
    ans2 = play_bingo(order, boards, version=2)  # 20774
    print(f"The last winning board has a final score of {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
