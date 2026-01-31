"""
Basic move validation to see if a move is legal
"""
import board, move, position, piece
from board import *
from move import *
from position import *
from piece import *


class MoveValidator:
    """Validates chess moves"""
    
    def __init__(self, board: Board):
        self.board = board
    
    def is_valid_move(self, move: Move) -> bool:
        """Check if a move is valid"""
        from_pos = move.from_pos
        to_pos = move.to_pos
        
        # Check if source has a piece
        piece_id = self.board.get_piece_id(from_pos)
        if piece_id == 0:
            return False
        
        piece = self.board.get_piece(from_pos)
        if piece is None:
            return False
        
        # Check if destination has a piece of the same colour
        dest_piece_id = self.board.get_piece_id(to_pos)
        if dest_piece_id != 0:
            dest_piece = self.board.get_piece(to_pos)
            if dest_piece and dest_piece.colour == piece.colour:
                return False
        
        # Check piece specific movement rules
        return self._is_valid_piece_move(piece, from_pos, to_pos)
    
    def _is_valid_piece_move(self, piece: Piece, from_pos: Position, to_pos: Position) -> bool:
        """Check if move is valid for the specific piece type"""
        row_diff = to_pos.row - from_pos.row
        col_diff = to_pos.col - from_pos.col
        
        if piece.type == PieceType.PAWN:
            return self._is_valid_pawn_move(piece, from_pos, to_pos, row_diff, col_diff)
        elif piece.type == PieceType.ROOK:
            return self._is_valid_rook_move(from_pos, to_pos, row_diff, col_diff)
        elif piece.type == PieceType.KNIGHT:
            return self._is_valid_knight_move(row_diff, col_diff)
        elif piece.type == PieceType.BISHOP:
            return self._is_valid_bishop_move(from_pos, to_pos, row_diff, col_diff)
        elif piece.type == PieceType.QUEEN:
            return self._is_valid_queen_move(from_pos, to_pos, row_diff, col_diff)
        elif piece.type == PieceType.KING:
            return self._is_valid_king_move(row_diff, col_diff)
        return False
    
    def _is_valid_pawn_move(self, piece: Piece, from_pos: Position, to_pos: Position, 
                           row_diff: int, col_diff: int) -> bool:
        """Validate pawn move"""
        direction = -1 if piece.colour == Colour.WHITE else 1
        
        # Forward move
        if col_diff == 0:
            # Single square forward
            if row_diff == direction and self.board.get_piece_id(to_pos) == 0:
                return True
            # Double square from starting position
            start_row = 6 if piece.colour == Colour.WHITE else 1
            if (from_pos.row == start_row and row_diff == 2 * direction and 
                self.board.get_piece_id(to_pos) == 0):
                # Check if path is clear
                mid_pos = Position(from_pos.row + direction, from_pos.col)
                return self.board.get_piece_id(mid_pos) == 0
        
        # Diagonal capture
        if abs(col_diff) == 1 and row_diff == direction:
            return self.board.get_piece_id(to_pos) != 0
        
        return False
    
    def _is_valid_rook_move(self, from_pos: Position, to_pos: Position, 
                           row_diff: int, col_diff: int) -> bool:
        """Validate rook move. Full lengths of rows or columns."""
        if row_diff != 0 and col_diff != 0:
            return False
        return self._is_path_clear(from_pos, to_pos)
    
    def _is_valid_knight_move(self, row_diff: int, col_diff: int) -> bool:
        """Validate knight move. 2 squares in any direction, then 1 square perpendicular."""
        return (abs(row_diff) == 2 and abs(col_diff) == 1) or \
               (abs(row_diff) == 1 and abs(col_diff) == 2)
    
    def _is_valid_bishop_move(self, from_pos: Position, to_pos: Position, 
                              row_diff: int, col_diff: int) -> bool:
        """Validate bishop move. Full lengths of diagonals."""
        if abs(row_diff) != abs(col_diff):
            return False
        return self._is_path_clear(from_pos, to_pos)
    
    def _is_valid_queen_move(self, from_pos: Position, to_pos: Position, 
                             row_diff: int, col_diff: int) -> bool:
        """Validate queen move. Full lengths of rows, columns, or diagonals."""
        if row_diff == 0 or col_diff == 0 or abs(row_diff) == abs(col_diff):
            return self._is_path_clear(from_pos, to_pos)
        return False
    
    def _is_valid_king_move(self, row_diff: int, col_diff: int) -> bool:
        """Validate king move. One square in any direction."""
        return abs(row_diff) <= 1 and abs(col_diff) <= 1
    
    def _is_path_clear(self, from_pos: Position, to_pos: Position) -> bool:
        """Check if path between two positions is clear (excluding destination)"""
        row_step = 0 if to_pos.row == from_pos.row else (1 if to_pos.row > from_pos.row else -1)
        col_step = 0 if to_pos.col == from_pos.col else (1 if to_pos.col > from_pos.col else -1)
        
        current_row = from_pos.row + row_step
        current_col = from_pos.col + col_step
        
        while current_row != to_pos.row or current_col != to_pos.col:
            if self.board.get_piece_id(Position(current_row, current_col)) != 0:
                return False
            current_row += row_step
            current_col += col_step
        
        return True
