"""
Chess board class
Board is 8x8 (Rows 0-7 and cols 0-7)
Row 0 is the top (black's starting side)
Row 7 is the bottom (white's starting side)
Uses unique piece IDs: 0 = empty, 1+ = piece IDs
"""
from typing import Optional
from .position import Position
from .piece import Piece, Colour, PieceType


class Board:
    
    def __init__(self):
        # Board stores piece IDs: 0 is empty, and anything 1 and above represents a unique piece
        self.squares: list[list[int]] = [
            [0 for _ in range(8)] for _ in range(8)
        ]
        # Registry mapping piece_id -> Piece info
        self.piece_registry: dict[int, Piece] = {}
        # Track next available piece ID
        self.next_piece_id: int = 1
    
    def _create_piece_id(self, piece_type: PieceType, colour: Colour) -> int:
        """Create a new piece and return its unique ID"""
        piece_id = self.next_piece_id
        self.next_piece_id += 1
        self.piece_registry[piece_id] = Piece(piece_type, colour)
        return piece_id
    
    def get_piece_id(self, position: Position) -> int:
        """Get piece ID at a position (0 if empty)"""
        return self.squares[position.row][position.col]
    
    def get_piece(self, position: Position) -> Optional[Piece]:
        """Get piece object at a position (None if empty)"""
        piece_id = self.get_piece_id(position)
        if piece_id == 0:
            return None
        return self.piece_registry.get(piece_id)
    
    def set_piece_id(self, position: Position, piece_id: int) -> None:
        """Set piece ID at a position (0 for empty)"""
        if piece_id != 0 and piece_id not in self.piece_registry:
            raise ValueError(f"Invalid piece ID: {piece_id}")
        self.squares[position.row][position.col] = piece_id
    
    def set_piece(self, position: Position, piece: Optional[Piece]) -> None:
        """Set piece at a position (creates new unique ID for each piece)"""
        if piece is None:
            self.set_piece_id(position, 0)
        else:
            # Always create a new unique ID for each piece instance
            piece_id = self._create_piece_id(piece.type, piece.colour)
            self.set_piece_id(position, piece_id)
    
    def initialise(self) -> None:
        """Initialise the board with the default starting position"""
        # Clear the board and registry
        for row in range(8):
            for col in range(8):
                self.squares[row][col] = 0
        self.piece_registry.clear()
        self.next_piece_id = 1
        
        # Place pawns
        for col in range(8):
            self.set_piece(Position(1, col), Piece(PieceType.PAWN, Colour.BLACK))
            self.set_piece(Position(6, col), Piece(PieceType.PAWN, Colour.WHITE))
        
        # Place back row pieces
        back_row_pieces = [
            PieceType.ROOK,
            PieceType.KNIGHT,
            PieceType.BISHOP,
            PieceType.QUEEN,
            PieceType.KING,
            PieceType.BISHOP,
            PieceType.KNIGHT,
            PieceType.ROOK
        ]
        
        for col in range(8):
            self.set_piece(Position(0, col), Piece(back_row_pieces[col], Colour.BLACK))
            self.set_piece(Position(7, col), Piece(back_row_pieces[col], Colour.WHITE))
    
    def copy(self) -> 'Board':
        """Create a copy of the board"""
        new_board = Board()
        # Copy squares
        for row in range(8):
            for col in range(8):
                new_board.squares[row][col] = self.squares[row][col]
        # Copy piece registry
        new_board.piece_registry = {
            piece_id: Piece(piece.type, piece.colour)
            for piece_id, piece in self.piece_registry.items()
        }
        new_board.next_piece_id = self.next_piece_id
        return new_board
