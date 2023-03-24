from board import Board
from game import Game
from ui import UI


obstruction_board = Board(6, 6)
game = Game(obstruction_board)
UI = UI(game, obstruction_board)
UI.keep_game_running()
