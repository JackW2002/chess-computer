from pieces import *

class chessGame():

    def __init__(self):
        self.p1_win = False
        self.p2_win = False
        self.board = []

    # Loads a board with the given FEN string
    def loadPos(self, fen: str):
        board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]

        column = 0
        row = 0
        for x in fen:
            if x == "q":
                board[row][column] = Queen("b")

            if x == "Q":
                board[row][column] = Queen("w")

            if x == "b":
                board[row][column] = Bishop("b")

            if x == "B":
                board[row][column] = Bishop("w")

            if x == "n":
                board[row][column] = Knight("b")

            if x == "N":
                board[row][column] = Knight("w")

            if x == "k":
                board[row][column] = King("b")

            if x == "K":
                board[row][column] = King("w")

            if x == "p":
                board[row][column] = Pawn("b")

            if x == "P":
                board[row][column] = Pawn("w")

            if x == "r":
                board[row][column] = Rook("b")

            if x == "R":
                board[row][column] = Rook("w")

            if x.isnumeric():
                column += int(x)
                continue

            column += 1

            if x == "/":
                row += 1
                column = 0
                
        self.board = board

    # Prints chess board to user
    def showBoard(self):
        board_view = "-------------------------------\n"
        for x in self.board:
            for y in x:
                if y:
                    board_view += " " + y.icon + " "
                else:
                    board_view += " • "
            board_view += "\n"
        return board_view

game = chessGame()
game.loadPos('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
print(game.showBoard())