from pieces import *
import copy

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

            piece = copy.copy(piece_dict[x])

            board[row][column] =  piece
            self.piece_pos[piece] = [column,row]
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

    def gen_moves(self):
        for x in self.board:
            for piece in x:
                if type(piece) == King:
                    moves = self.gen_king(piece)
        return moves

    # Returns possible moves
    def gen_king(self, king: King):
        position = self.piece_pos[king]
        moves_unculled = [[position[0]-1,position[1]+1], [position[0],position[1]+1], [position[0]+1,position[1]+1],
                        [position[0]-1,position[1]], [position[0]+1,position[1]], [position[0]-1,position[1]-1],
                        [position[0],position[1]-1],[position[0]+1,position[1]-1]]

        moves = moves_unculled
        for move in moves_unculled:
            if move[0] > 8 or move[0] < 0:
                moves.remove(move)
                continue
            if move[1] > 8 or move[1] < 0:
                moves.remove(move)
        
        print(str(king) + str(moves))
        return moves


game = chessGame()
game.load_pos("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
print(game.show_board())
game.gen_moves()
# make dict of all pieces (key) and there corrosponding locations whichh will be updated when piece class moves
