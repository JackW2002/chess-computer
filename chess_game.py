from pieces import *


class chessGame:
    def __init__(self):
        self.p1_win = False
        self.p2_win = False
        self.board = []
        self.piece_pos = {}

    # Loads a board with the given FEN string
    def load_pos(self, fen: str):
        # Make empty board to add too
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

        piece_dict = {
            "k": King("b"),
            "K": King("w"),
            "q": Queen("b"),
            "Q": Queen("w"),
            "b": Bishop("b"),
            "B": Bishop("w"),
            "n": Knight("b"),
            "N": Knight("w"),
            "r": Rook("b"),
            "R": Rook("w"),
            "p": Pawn("b"),
            "P": Pawn("w"),
        }

        # Go through fen string adding pieces
        for x in fen:

            if x.isnumeric():
                column += int(x)
                continue

            if x == "/":
                row += 1
                column = 0
                continue

            board[row][column] = piece_dict[x]
            column += 1

        self.board = board

    # Returns readable string of chess board
    def show_board(self):
        board_view = "-------------------------------\n"
        for row in self.board:
            for square in row:
                if square is not None:
                    board_view += " " + str(square) + " "
                else:
                    board_view += " • "
            board_view += "\n"
        return board_view

    def gen_moves(self, board):
        y = 0
        x = 0
        for x in board:
            for piece in x:
                if type(piece) == King:
                    gen_king(piece, x, y)
            x = +1
        y = +1

    def gen_king(self, king: King, posX: int, posY: int):
        pass


game = chessGame()
game.load_pos("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
print(game.show_board())

# make dict of all pieces (key) and there corrosponding locations whichh will be updated when piece class moves
