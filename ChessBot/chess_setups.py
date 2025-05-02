from enum import Enum, IntEnum


class PieceType(IntEnum):
    NULL = 0
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6


class PieceColor(IntEnum):
    NULL = 0
    WHITE = 1
    BLACK = 2


class Piece(Enum):
    NULL = (PieceColor.NULL, PieceType.NULL)

    WHITE_PAWN = (PieceColor.WHITE, PieceType.PAWN)
    WHITE_ROOK = (PieceColor.WHITE, PieceType.ROOK)
    WHITE_KNIGHT = (PieceColor.WHITE, PieceType.KNIGHT)
    WHITE_BISHOP = (PieceColor.WHITE, PieceType.BISHOP)
    WHITE_QUEEN = (PieceColor.WHITE, PieceType.QUEEN)
    WHITE_KING = (PieceColor.WHITE, PieceType.KING)

    BLACK_PAWN = (PieceColor.BLACK, PieceType.PAWN)
    BLACK_ROOK = (PieceColor.BLACK, PieceType.ROOK)
    BLACK_KNIGHT = (PieceColor.BLACK, PieceType.KNIGHT)
    BLACK_BISHOP = (PieceColor.BLACK, PieceType.BISHOP)
    BLACK_QUEEN = (PieceColor.BLACK, PieceType.QUEEN)
    BLACK_KING = (PieceColor.BLACK, PieceType.KING)

    @property
    def color(self):
        return self.value[0]

    @property
    def type(self):
        return self.value[1]


class Board:
    def __init__(self):
        board_size = 64
        self.square = [Piece.NULL] * board_size

        # temp debug
        self.square[0] = Piece.WHITE_BISHOP
        self.square[63] = Piece.BLACK_QUEEN
        self.square[7] = Piece.BLACK_KNIGHT

