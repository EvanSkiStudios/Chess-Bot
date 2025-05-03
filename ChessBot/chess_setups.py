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


def board_from_fen(board: list, fen_string: str):
    fen_map = {
        'p': Piece.BLACK_PAWN,
        'q': Piece.BLACK_QUEEN,
        'r': Piece.BLACK_ROOK,
        'n': Piece.BLACK_KNIGHT,
        'b': Piece.BLACK_BISHOP,
        'k': Piece.BLACK_KING,

        'P': Piece.WHITE_PAWN,
        'Q': Piece.WHITE_QUEEN,
        'R': Piece.WHITE_ROOK,
        'N': Piece.WHITE_KNIGHT,
        'B': Piece.WHITE_BISHOP,
        'K': Piece.WHITE_KING,
    }

    board_starting_pos_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    if fen_string == "":
        fen_string = board_starting_pos_FEN

    fen_board = fen_string.split(' ')[0]

    row, col = 0, 0
    for symbol in fen_board:
        if symbol == '/':
            row += 1
            col = 0
        else:
            if symbol.isdigit():
                col += int(symbol)
            else:
                board[row][col] = fen_map.get(symbol, f"Unknown({symbol})")
                col += 1

    return board


class ChessBoard:
    def __init__(self):
        rows, cols = (8, 8)
        self.square = [[Piece.NULL for _ in range(cols)] for _ in range(rows)]

    def default_board_start(self):
        self.square = board_from_fen(self.square, "")

    def debug_board(self):
        self.square = board_from_fen(self.square, "r1bk3r/p2pBpNp/n4n2/1p1NP2P/6P1/3P4/P1P1K3/q5b1")
