import numpy as np
import random

BOARD_SIZE = 9
MINE_NUMBER = 10

def update_numbers_on_board(array, row_index, col_index):
    for i in range(max(0, row_index-1), min(BOARD_SIZE, row_index + 2)):
        for j in range(max(0, col_index-1), min(BOARD_SIZE, col_index + 2)):
            if not isinstance(array[i, j], Mine):
                array[i, j] += 1
    # array[max(0, row_index-1):row_index + 2, max(0, col_index-1):col_index + 2] += 1
    return array


def randomize_board():
    array = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=object)
    mines_indices = random.sample(range(BOARD_SIZE * BOARD_SIZE), MINE_NUMBER)
    for idx in mines_indices:
        row_index, col_index = idx // BOARD_SIZE, idx % BOARD_SIZE
        array = update_numbers_on_board(array, row_index, col_index)
        array[row_index, col_index] = Mine()
    return array


def print_board(array):
    for row in array:
        print(list(map(str, row)))


class Mine:
    def __init__(self):
        pass

    def __str__(self):
        return "*"


class Flag:
    def __init__(self):
        pass


class Number:
    def __init__(self):
        pass


class Cell:
    def __init__(self):
        self.is_revealed = False
        self.type = False


class MinesweeperBoard:
    def __init__(self, num_rows, num_columns):
        self.full_board = []
        self.revealed_board = []


if __name__ == '__main__':
    board = randomize_board()
    print_board(board)