"""
Chess piece representation
"""
from enum import Enum


class Colour(Enum):
    """Piece colours"""
    WHITE = "white"
    BLACK = "black"
    
    @classmethod
    def opposite(cls, colour: 'Colour') -> 'Colour':
        """Get the opposite colour"""
        return cls.BLACK if colour == cls.WHITE else cls.WHITE


class PieceType(Enum):
    """Piece types"""
    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"


class Piece:
    """Chest piece class."""
    def __init__(self, piece_type: PieceType, colour: Colour):
        self.type = piece_type
        self.colour = colour
