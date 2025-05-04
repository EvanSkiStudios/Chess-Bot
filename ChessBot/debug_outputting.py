from board_data import PieceType, PieceColor, Piece


def piece_symbol(piece):
    symbols = {
        (PieceColor.WHITE, PieceType.PAWN): '♙',
        (PieceColor.WHITE, PieceType.ROOK): '♖',
        (PieceColor.WHITE, PieceType.KNIGHT): '♘',
        (PieceColor.WHITE, PieceType.BISHOP): '♗',
        (PieceColor.WHITE, PieceType.QUEEN): '♕',
        (PieceColor.WHITE, PieceType.KING): '♔',

        (PieceColor.BLACK, PieceType.PAWN): '♟',
        (PieceColor.BLACK, PieceType.ROOK): '♜',
        (PieceColor.BLACK, PieceType.KNIGHT): '♞',
        (PieceColor.BLACK, PieceType.BISHOP): '♝',
        (PieceColor.BLACK, PieceType.QUEEN): '♛',
        (PieceColor.BLACK, PieceType.KING): '♚',
    }

    if piece is None or piece == Piece.NULL:
        return '·'  # empty square
    return symbols.get((piece.color, piece.type), '?')


def print_board_debug(board):
    print("  A B C D E F G H")
    for row in range(7, -1, -1):
        rank = row + 1
        line = f"{rank} "
        for col in range(8):
            piece = board[row][col]
            line += piece_symbol(piece) + " "
        print(line)
    print("  A B C D E F G H")
