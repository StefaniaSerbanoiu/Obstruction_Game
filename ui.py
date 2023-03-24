class UI:
    def __init__(self, game, board):
        self.__game = game
        self.__board = board

    def introduce_coordinates(self):
        print("Introduce coordinate X:")
        try:
            x = int(input())
        except:
            x = -1
        print("Introduce coordinate Y:")
        try:
            y = int(input())
        except:
            y = -1
        return [x - 1, y - 1]

    def player_move(self):
        print("Player's move:\n")
        x, y = self.introduce_coordinates()
        if x >= 0 and y >= 0:
            self.__game.move_player(x, y)
        else:
            print("Player lost its turn because of incorrect input!!!!!!!!")

    def computer_move(self):
        print("Computer's move:\n")
        self.__game.move_computer()

    def keep_game_running(self):
        turn = 0
        game_stopped = self.__board.is_game_won()
        print(self.__board)
        while game_stopped is False:

            if turn % 2 == 0:
                self.player_move()
            else:
                self.computer_move()
            turn += 1
            game_stopped = self.__board.is_game_won()

            print(self.__board)
        self.result(turn)

    def result(self, turn):
        if turn % 2 == 0:
            print("THE COMPUTER WON")
        else:
            print("you won")

    def print_rules(self):
        print("In a turn, a player will choose a position on the board,")





