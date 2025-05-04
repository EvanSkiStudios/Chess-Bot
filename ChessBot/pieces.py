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


# Central piece-symbol-letter mapping
_PIECE_INFO = {
    ('WHITE', 'PAWN'):    ('♙', 'P'),
    ('WHITE', 'ROOK'):    ('♖', 'R'),
    ('WHITE', 'KNIGHT'):  ('♘', 'N'),
    ('WHITE', 'BISHOP'):  ('♗', 'B'),
    ('WHITE', 'QUEEN'):   ('♕', 'Q'),
    ('WHITE', 'KING'):    ('♔', 'K'),

    ('BLACK', 'PAWN'):    ('♟', 'p'),
    ('BLACK', 'ROOK'):    ('♜', 'r'),
    ('BLACK', 'KNIGHT'):  ('♞', 'n'),
    ('BLACK', 'BISHOP'):  ('♝', 'b'),
    ('BLACK', 'QUEEN'):   ('♛', 'q'),
    ('BLACK', 'KING'):    ('♚', 'k'),
}

# Build all maps from central data
symbol_to_piece_map = {}
letter_to_piece_map = {}
piece_to_symbol_map = {}
piece_to_letter_map = {}

for (color, ptype), (symbol, letter) in _PIECE_INFO.items():
    piece = getattr(Piece, f"{color}_{ptype}")
    piece_to_symbol_map[piece] = symbol
    piece_to_letter_map[piece] = letter
    symbol_to_piece_map[symbol] = piece
    letter_to_piece_map[letter] = piece


# Conversion functions
def piece_to_symbol(piece):
    if piece is None or piece == Piece.NULL:
        return '.'
    return piece_to_symbol_map.get(piece, '?')


def symbol_to_piece(symbol: str):
    return symbol_to_piece_map.get(symbol, f"Unknown({symbol})")


def letter_to_piece(letter: str):
    return letter_to_piece_map.get(letter, f"Unknown({letter})")


def piece_to_letter(piece):
    return piece_to_letter_map.get(piece, f"Unknown({piece})")
