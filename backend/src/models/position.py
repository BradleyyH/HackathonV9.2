class Position:
    """Represents a position on the chess board using matrix notation (row, col)"""
    
    def __init__(self, row: int, col: int):
        if not (0 <= row <= 7 and 0 <= col <= 7):
            raise ValueError(f"Invalid position")
        self.row = row
        self.col = col
    
    def __eq__(self, other: 'Position') -> bool:
        """Check if two positions are equal"""
        if not isinstance(other, Position):
            return False
        return self.row == other.row and self.col == other.col
