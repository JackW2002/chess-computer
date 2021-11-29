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

            board[row][column] = piece
            self.piece_pos[piece] = [column, row, piece.colour]
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
        moves = 0
        for x in self.board:
            for piece in x:
                # if type(piece) == King:
                #     moves = self.gen_king(piece)
                # if type(piece) == Rook:
                #     moves = self.gen_rook(piece)
                # if type(piece) == Bishop:
                #     moves = self.gen_bishop(piece)
                if type(piece) == Queen:
                    moves = self.gen_queen(piece)
        return moves

    # Returns possible moves
    def gen_king(self, king: King):
        position = self.piece_pos[king]

        moves_unculled = [
            [position[0] - 1, position[1] + 1],
            [position[0], position[1] + 1],
            [position[0] + 1, position[1] + 1],
            [position[0] - 1, position[1]],
            [position[0] + 1, position[1]],
            [position[0] - 1, position[1] - 1],
            [position[0], position[1] - 1],
            [position[0] + 1, position[1] - 1],
        ]

        valid_moves = []
        for move in moves_unculled:
            if (
                move[0] > 7
                or move[0] < 0
                or move[1] > 7
                or move[1] < 0
                or move in self.piece_pos.values()
            ):
                continue
            else:
                valid_moves.append(move)

        print(str(king) + str(valid_moves))
        return valid_moves

    def gen_queen(self, queen: Queen):

        valid_moves = self.gen_rook(queen) + self.gen_bishop(queen)

        return valid_moves


    def gen_rook(self, rook):

        pos_x = self.piece_pos[rook][0]

        pos_y = self.piece_pos[rook][1]

        valid_moves = []

        distance = 1

        # Check right of rook for valid moves
        while pos_x + distance < 8:
            # Check if there is a piece in location if there is check colour
            if self.board[pos_y][pos_x + distance]:
                if self.board[pos_y][pos_x + distance].colour == rook.colour:
                    break
                valid_moves.append([pos_x + distance, pos_y])
                break

            # If no piece on square add to valid and check next
            valid_moves.append([pos_x + distance, pos_y])
            distance += 1

        # Check left of rook for valid moves
        distance = 1
        while pos_x - distance >= 0:
            # Check if there is a piece in location if there is check colour
            if self.board[pos_y][pos_x - distance]:
                if self.board[pos_y][pos_x - distance].colour == rook.colour:
                    break
                valid_moves.append([pos_x - distance, pos_y])
                break

            # If no piece on square add to valid and check next
            valid_moves.append([pos_x - distance, pos_y])
            distance += 1

        # Check above of rook for valid moves
        distance = 1
        while pos_y - distance >= 0:
            # Check if there is a piece in location if there is check colour
            if self.board[pos_y - distance][pos_x]:
                if self.board[pos_y - distance][pos_x].colour == rook.colour:
                    break
                valid_moves.append([pos_x, pos_y - distance])
                break

            # If no piece on square add to valid and check next
            valid_moves.append([pos_x, pos_y - distance])
            distance += 1

        # Check below of rook for valid moves
        distance = 1
        while pos_y + distance < 8:
            # Check if there is a piece in location if there is check colour
            if self.board[pos_y + distance][pos_x]:
                if self.board[pos_y + distance][pos_x].colour == rook.colour:
                    break
                valid_moves.append([pos_x, pos_y + distance])
                break

            # If no piece on square add to valid and check next
            valid_moves.append([pos_x, pos_y + distance])
            distance += 1

        print(str(rook) + str(valid_moves))

        return valid_moves

    def gen_bishop(self, bishop):

        pos_x = self.piece_pos[bishop][0]

        pos_y = self.piece_pos[bishop][1]

        valid_moves = []

        distance = 1

        # Check top-right of bishop for valid moves
        while pos_x + distance < 8 and pos_y - distance >= 0:
            # Check if there is a piece in location if there is check colour
            if self.board[pos_y - distance][pos_x + distance]:
                if self.board[pos_y - distance][pos_x + distance].colour == bishop.colour:
                    break
                valid_moves.append([pos_x + distance, pos_y - distance])
                break

            # If no piece on square add to valid and check next
            valid_moves.append([pos_x + distance, pos_y - distance])
            distance += 1

        # Check top-left of bishop for valid moves
        distance = 1
        while pos_x - distance >= 0 and pos_y - distance >=0:
            # Check if there is a piece in location if there is check colour
            if self.board[pos_y - distance][pos_x - distance]:
                if self.board[pos_y - distance][pos_x - distance].colour == bishop.colour:
                    break
                valid_moves.append([pos_x - distance, pos_y - distance])
                break

            # If no piece on square add to valid and check next
            valid_moves.append([pos_x - distance, pos_y - distance])
            distance += 1

        # Check bottom-left of bishop for valid moves
        distance = 1
        while pos_x - distance >= 0 and pos_y + distance < 8:
            # Check if there is a piece in location if there is check colour
            if self.board[pos_y + distance][pos_x - distance]:
                if self.board[pos_y + distance][pos_x - distance].colour == bishop.colour:
                    break
                valid_moves.append([pos_x - distance, pos_y + distance])
                break

            # If no piece on square add to valid and check next
            valid_moves.append([pos_x - distance, pos_y + distance])
            distance += 1

        # Check bottom-right of bishop for valid moves
        distance = 1
        while pos_y + distance < 8 and pos_x + distance < 8:
            # Check if there is a piece in location if there is check colour
            if self.board[pos_y + distance][pos_x + distance]:
                if self.board[pos_y + distance][pos_x + distance].colour == bishop.colour:
                    break
                valid_moves.append([pos_x + distance, pos_y + distance])
                break

            # If no piece on square add to valid and check next
            valid_moves.append([pos_x + distance, pos_y + distance])
            distance += 1

        print(str(bishop) + str(valid_moves))

        return valid_moves

game = chessGame()
# game.load_pos("rnbqkbnr/ppp1pppp/8/3p4/7P/7R/PPPPPPP1/RNBQKBN1")
# game.load_pos("8/8/8/2P1r1P1/8/8/4p3/8")
# game.load_pos("b2B/8/8/8/8/8/8/8")
# game.load_pos("8/4P3/5BP1/8/4b2n/2p5/8/8")
game.load_pos("rn1qkbnr/ppp1pppp/8/3p4/4P1b1/8/PPPP1PPP/RNBQKBNR")
print(game.show_board())
game.gen_moves()
# make dict of all pieces (key) and there corrosponding locations whichh will be updated when piece class moves
