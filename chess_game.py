from pieces import *
import copy
import time


class chessGame:
    def __init__(self):
        self.p1_win = False
        self.p2_win = False
        self.board = []
        self.piece_pos = {}
        self.en_pass = []

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

            if type(piece) == Pawn and (row != 1 and row != 6):
                piece.has_moved = True

            board[row][column] = piece
            self.piece_pos[piece] = [column, row, piece.colour]
            column += 1

        self.board = board

    # Returns readable string of chess board
    def show_board(self):
        board_view = "-------------------------------\n  0 1 2 3 4 5 6 7\n"
        num = 0
        for row in self.board:
            board_view += str(num) + " "
            num += 1
            for square in row:
                if square is not None:
                    board_view += "" + str(square) + " "
                else:
                    board_view += "• "
            board_view += "\n"
        return board_view

    def gen_moves(self):
        moves = 0
        for x in self.board:
            for piece in x:
                if type(piece) == King:
                    moves = self.gen_king(piece)
                if type(piece) == Rook:
                    moves = self.gen_rook(piece)
                if type(piece) == Bishop:
                    moves = self.gen_bishop(piece)
                if type(piece) == Queen:
                    moves = self.gen_queen(piece)
                if type(piece) == Knight:
                    moves = self.gen_knight(piece)
                if type(piece) == Pawn:
                    moves = self.gen_pawn(piece)
        return moves

    # Generates moves for kings and returns them in list
    def gen_king(self, king: King):
        pos_x = self.piece_pos[king][0]
        pos_y = self.piece_pos[king][1]

        moves_unvalidated = []

        # generate possible within board moves
        if pos_y - 1 >= 0:
            moves_unvalidated.append([pos_x, pos_y - 1])
            if pos_x - 1 >= 0:
                moves_unvalidated.append([pos_x - 1, pos_y - 1])
            if pos_x + 1 < 8:
                moves_unvalidated.append([pos_x + 1, pos_y - 1])
        if pos_x - 1 >= 0:
            moves_unvalidated.append([pos_x - 1, pos_y])
        if pos_x + 1 < 8:
            moves_unvalidated.append([pos_x + 1, pos_y])
        if pos_y + 1 < 8:
            moves_unvalidated.append([pos_x, pos_y + 1])
            if pos_x - 1 >= 0:
                moves_unvalidated.append([pos_x - 1, pos_y + 1])
            if pos_x + 1 < 8:
                moves_unvalidated.append([pos_x + 1, pos_y + 1])

        valid_moves = []
        for move in moves_unvalidated:
            if self.board[move[1]][move[0]] != None:
                if self.board[move[1]][move[0]].colour == king.colour:
                    continue
            valid_moves.append(move)

        print(str(king) + str(valid_moves))
        return valid_moves

    # Generates moves for queens and returns them in list
    def gen_queen(self, queen: Queen):

        valid_moves = self.gen_rook(queen) + self.gen_bishop(queen)

        return valid_moves

    # Generates moves for rook and returns them in list
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

    # Generates moves for bishops and returns them in list
    def gen_bishop(self, bishop):

        pos_x = self.piece_pos[bishop][0]

        pos_y = self.piece_pos[bishop][1]

        valid_moves = []

        distance = 1

        # Check top-right of bishop for valid moves
        while pos_x + distance < 8 and pos_y - distance >= 0:
            # Check if there is a piece in location if there is check colour
            if self.board[pos_y - distance][pos_x + distance]:
                if (
                    self.board[pos_y - distance][pos_x + distance].colour
                    == bishop.colour
                ):
                    break
                valid_moves.append([pos_x + distance, pos_y - distance])
                break

            # If no piece on square add to valid and check next
            valid_moves.append([pos_x + distance, pos_y - distance])
            distance += 1

        # Check top-left of bishop for valid moves
        distance = 1
        while pos_x - distance >= 0 and pos_y - distance >= 0:
            # Check if there is a piece in location if there is check colour
            if self.board[pos_y - distance][pos_x - distance]:
                if (
                    self.board[pos_y - distance][pos_x - distance].colour
                    == bishop.colour
                ):
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
                if (
                    self.board[pos_y + distance][pos_x - distance].colour
                    == bishop.colour
                ):
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
                if (
                    self.board[pos_y + distance][pos_x + distance].colour
                    == bishop.colour
                ):
                    break
                valid_moves.append([pos_x + distance, pos_y + distance])
                break

            # If no piece on square add to valid and check next
            valid_moves.append([pos_x + distance, pos_y + distance])
            distance += 1

        print(str(bishop) + str(valid_moves))

        return valid_moves

    # Generates moves for knigts and returns them in list
    def gen_knight(self, knight):

        pos_x = self.piece_pos[knight][0]
        pos_y = self.piece_pos[knight][1]

        possible_moves = []

        # Check squares above knight
        if pos_y - 1 >= 0:
            # Check square to right
            if pos_x + 2 < 8:
                possible_moves.append([pos_x + 2, pos_y - 1])
            # Check square to left
            if pos_x - 2 >= 0:
                possible_moves.append([pos_x - 2, pos_y - 1])

            if pos_y - 2 >= 0:
                # Check square to right
                if pos_x + 1 < 8:
                    possible_moves.append([pos_x + 1, pos_y - 2])
                # Check square to left
                if pos_x - 1 >= 0:
                    possible_moves.append([pos_x - 1, pos_y - 2])

        # Check squares below knight
        if pos_y + 1 < 8:
            # Check square to right
            if pos_x + 2 < 8:
                possible_moves.append([pos_x + 2, pos_y + 1])
            # Check square to left
            if pos_x - 2 >= 0:
                possible_moves.append([pos_x - 2, pos_y + 1])

            if pos_y + 2 < 8:
                # Check square to right
                if pos_x + 1 < 8:
                    possible_moves.append([pos_x + 1, pos_y + 2])
                # Check if square to left
                if pos_x - 1 >= 0:
                    possible_moves.append([pos_x - 1, pos_y + 2])

        valid_moves = []

        for move in possible_moves:
            if move + [knight.colour] in self.piece_pos.values():
                continue
            valid_moves.append(move)

        print(str(knight) + str(valid_moves))

        return valid_moves

    # Generates moves for pawns and returns them in list
    def gen_pawn(self, pawn):

        valid_moves = []
        pos_x = self.piece_pos[pawn][0]
        pos_y = self.piece_pos[pawn][1]
        direction = 1
        opp_colour = "w"

        # Check if pawn can move forwards
        # Check pawn colour for direction
        if pawn.colour == "w":
            direction = -1
            opp_colour = "b"
        # see if pawn can be pushed
        if pos_y + direction < 8 and self.board[pos_y + direction][pos_x] == None:
            valid_moves.append([pos_x, pos_y + direction])
            # see if pawn can be pushed 2 squares
            if (
                pos_y + direction < 8
                and self.board[pos_y + direction + direction][pos_x] == None
                and pawn.has_moved == False
            ):
                valid_moves.append([pos_x, pos_y + direction + direction])

        # Check if pawn can take right
        if [pos_x + 1, pos_y + direction, opp_colour] in self.piece_pos.values():
            valid_moves.append([pos_x + 1, pos_y + direction])
        # Check if pawn can take right
        if [pos_x - 1, pos_y + direction, opp_colour] in self.piece_pos.values():
            valid_moves.append([pos_x - 1, pos_y + direction])


        if self.board[pos_y][pos_x+1] != None:
            if  self.board[pos_y][pos_x+1].en_passant:
                valid_moves.append([pos_x+1,pos_y-1]) 

            if self.board[pos_y][pos_x-1] != None:
                if self.board[pos_y][pos_x-1].en_passant:
                    valid_moves.append([pos_x-1,pos_y-1]) 

        print(
            str(pawn)
            + "location: "
            + str([pos_x, pos_y])
            + " moves: "
            + str(valid_moves)
        )
        return valid_moves

    # plys chess game
    def play_game(self):
        self.load_pos("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
        while self.p1_win == False and self.p2_win == False:
            self.p1_move()
            self.p2_move()

    # Player 1 enter move
    def p1_move(self):
        print(self.show_board())
        print(str(self.en_pass))
        print("P1: input move")
        str_p1_move = input("")
        p1_piece_pos = [int(str_p1_move[0]), int(str_p1_move[2])]
        p1_piece = self.board[p1_piece_pos[1]][p1_piece_pos[0]]
        p1_move = [int(str_p1_move[4]), int(str_p1_move[6])]
        if not self.valiate_move(p1_piece, p1_move):
            print("ERROR RE-ENTER MOVE")
            self.p1_move()
        self.move(p1_piece, p1_move)

    # Player 2 enter move
    def p2_move(self):
        print(self.show_board())
        print(str(self.en_pass))
        print("P2: input move")
        str_p2_move = input("")
        p2_piece_pos = [int(str_p2_move[0]), int(str_p2_move[2])]
        p2_piece = self.board[p2_piece_pos[1]][p2_piece_pos[0]]
        p2_move = [int(str_p2_move[4]), int(str_p2_move[6])]
        if not self.valiate_move(p2_piece, p2_move):
            print("ERROR RE-ENTER MOVE")
            self.p2_move()
        self.move(p2_piece, p2_move)

    # Checks weather move entered is valid
    def valiate_move(self, piece, move):
        if piece == None:
            return False
        if type(piece) == King:
            valid_moves = self.gen_king(piece)
        if type(piece) == Rook:
            valid_moves = self.gen_rook(piece)
        if type(piece) == Bishop:
            valid_moves = self.gen_bishop(piece)
        if type(piece) == Queen:
            valid_moves = self.gen_queen(piece)
        if type(piece) == Knight:
            valid_moves = self.gen_knight(piece)
        if type(piece) == Pawn:
            valid_moves = self.gen_pawn(piece)

        if move not in valid_moves:
            return False
        return True

    # Move piece to desired position and delete origional pos
    def move(self, piece, pos):

        origional_pos = self.piece_pos[piece]
        dead_piece = self.board[pos[1]][pos[0]]
        self.board[pos[1]][pos[0]] = piece
        if dead_piece != None:
            del self.piece_pos[dead_piece]
        new_pos = {piece: [pos[0], pos[1], piece.colour]}
        self.piece_pos.update(new_pos)
        self.board[origional_pos[1]][origional_pos[0]] = None


        for pawn in self.en_pass:
            pawn.en_passant = False
        self.en_pass = []
        if type(piece) == Pawn:
            piece.has_moved = True
            if origional_pos[0] != pos[0]:
                if piece.colour == 'w':
                    del self.piece_pos[self.board[pos[1]+1][pos[0]]]
                    self.board[pos[1]+1][pos[0]] = None
                if piece.colour == 'b':
                    del self.piece_pos[self.board[pos[1]-1][pos[0]]]
                    self.board[pos[1]-1][pos[0]] = None
            if abs(origional_pos[1] - pos[1]) == 2:
                piece.en_passant = True
                self.en_pass.append(piece)



game = chessGame()
# game.load_pos("rnbqkbnr/ppp1pppp/8/3p4/7P/7R/PPPPPPP1/RNBQKBN1")
# game.load_pos("8/8/8/2P1r1P1/8/8/4p3/8")
# game.load_pos("b2B/8/8/8/8/8/8/8")
# game.load_pos("8/4P3/5BP1/8/4b2n/2p5/8/8")
# game.load_pos("r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1")
# game.load_pos("n6n/8/8/8/8/8/8/n6n")
# game.load_pos("6n1/8/5Q1p/3P4/8/4N3/6b1/8")
# game.load_pos("8/2p3p1/1p1kB3/8/7P/8/5PP1/6K1")
# print(game.show_board())
# game.gen_moves()
# game.move(game.board[0][0], [5,5])
# print(game.show_board())
# make dict of all pieces (key) and there corrosponding locations whichh will be updated when piece class moves
game.play_game()
