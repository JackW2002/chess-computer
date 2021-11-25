from abc import ABC, abstractmethod
from enum import Enum


class Piece(ABC):
    @abstractmethod
    def move(self):
        pass



class Colour(Enum):
    WHITE = 0
    BLACK = 1


class Queen(Piece):
    def __init__(self, colour):
        self.colour = colour
        if self.colour == "w":
            self.icon = "♕"
        else:
            self.icon = "♛"

    def move(self):
        pass



class Rook(Piece):
    def __init__(self, colour):
        self.colour = colour
        if self.colour == "w":
            self.icon = "♖"
        else:
            self.icon = "♜"

    def move(self):
        pass


class King(Piece):
    def __init__(self, colour):
        self.colour = colour
        if self.colour == "w":
            self.icon = "♔"
        else:
            self.icon = "♛"
        self.canCastle = True

    def move(self):
        pass



class Pawn(Piece):
    def __init__(self, colour):
        self.colour = colour
        if self.colour == "w":
            self.icon = "♙"
        else:
            self.icon = "♟︎"

    def move(self):
        pass



class Knight(Piece):
    def __init__(self, colour):
        self.colour = colour
        if self.colour == "w":
            self.icon = "♘"
        else:
            self.icon = "♞"

    def move(self):
        pass

    def genMoves(self):
        pass


class Bishop(Piece):
    def __init__(self, colour):
        self.colour = colour
        if self.colour == "w":
            self.icon = "♗"
        else:
            self.icon = "♝"
    def __str__(self):
        return()
    

    def move(self):
        pass

    def genMoves(self):
        pass
