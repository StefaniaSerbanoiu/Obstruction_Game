from random import shuffle
from board import *


class Game:
    def __init__(self, board):
        self.__board = board

    def move_player(self, x, y):
        if self.__board.is_cell_free(x, y):
            self.__board.default_move(x, y, False)
            self.__board.get_board_position(x, y).is_o = True
            self.__board.get_board_position(x, y).is_free = False

    def computer_choice(self):
        choices_choices = []
        for row in range(6):
            for column in range(6):
                if self.__board.get_board_position(row, column).is_free is True:
                    choices_choices.append([row, column])
        shuffle(choices_choices)
        return [choices_choices[0][0], choices_choices[0][1]]

    def move_computer(self):
        x, y = self.computer_choice()
        self.__board.default_move(x, y, True)
        self.__board.get_board_position(x, y).is_x = True
        self.__board.get_board_position(x, y).is_free = False
