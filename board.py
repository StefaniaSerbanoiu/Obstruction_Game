import random
from texttable import Texttable
from cell import Cell


class Board:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns

        self._board = [[Cell() for index_1 in range(self._columns)] for index_2 in range(self._rows)]

    def __str__(self):
        table = Texttable()

        header = list(range(1, self._columns + 1))
        table.header(['0'] + header)

        for row in range(self._rows):
            table.add_row([str(row + 1)] + self._board[row])
        return table.draw()

    def get_board_position(self, x, y):
        return self._board[x][y]

    def occupy_adjacent_positions(self, x, y):
        if x - 1 > 0:
            if y - 1 > 0:
                self._board[x - 1][y - 1].is_free = False
                self._board[x - 1][y - 1].blocked = True
            self._board[x - 1][y].is_free = False
            self._board[x - 1][y].blocked = True
            if y + 1 < self._columns:
                self._board[x - 1][y + 1].is_free = False
                self._board[x - 1][y + 1].blocked = True
        if x + 1 < self._rows:
            if y - 1 > 0:
                self._board[x + 1][y - 1].is_free = False
                self._board[x + 1][y - 1].blocked = True
            self._board[x + 1][y].is_free = False
            self._board[x + 1][y].blocked = True
            if y + 1 < self._columns:
                self._board[x + 1][y + 1].is_free = False
                self._board[x + 1][y + 1].blocked = True
        if y + 1 < self._columns:
            self._board[x][y + 1].is_free = False
            self._board[x][y + 1].blocked = True
        if y - 1 > 0:
            self._board[x][y - 1].is_free = False
            self._board[x][y - 1].blocked = True

    def default_move(self, x, y, is_x):
        cell = self._board[x][y]
        if self.is_cell_free(x, y):
            if is_x is True:
                cell.is_x = True
                cell.content = "X"
            else:
                cell.is_o = True
                cell.content = "O"
            self.occupy_adjacent_positions(x, y)
        else:
            print("Invalid position!!!")

    def is_cell_free(self, x, y):
        cell = self._board[x][y]
        if cell.is_free is True:
            return True
        return False

    def is_game_won(self):
        for index_1 in range(self._rows):
            for index_2 in range(self._columns):
                if self.is_cell_free(index_1, index_2) is True:
                    return False
        return True





