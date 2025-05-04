from pieces import letter_to_piece, Piece


def board_from_fen(board: list, fen_string: str):

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
                board[row][col] = letter_to_piece(symbol)
                col += 1

    return board


class ChessBoard:
    def __init__(self):
        rows, cols = (8, 8)
        self.squares = [[Piece.NULL for _ in range(cols)] for _ in range(rows)]

    def default_board_start(self):
        self.squares = board_from_fen(self.squares, "")

    def debug_board(self):
        self.squares = board_from_fen(self.squares, "r1bk3r/p2p1pNp/n2B1n2/1p1NP2P/6P1/3P4/P1P1K3/q5b1 w - - 0 1")


def algebraic_to_index(square: str) -> tuple[int, int]:
    """
    Converts algebraic notation (e.g., 'E2') to board indices [row][col].
    'A1' -> (0, 0), 'H8' -> (7, 7)
    """
    file = square[0].upper()
    rank = int(square[1])
    col = ord(file) - ord('A')
    row = rank - 1
    return row, col


def index_to_algebraic(row: int, col: int) -> str:
    """
    Converts board indices [row][col] to algebraic notation.
    (0, 0) -> 'A1', (7, 7) -> 'H8'
    """
    file = chr(ord('A') + col)
    rank = row + 1
    return f"{file}{rank}"

