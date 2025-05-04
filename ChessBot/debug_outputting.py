from pieces import piece_to_symbol


def print_board_debug(board):
    print("\n=================================")
    print("   A B C D E F G H")
    for row in range(8):
        rank = 8 - row  # Now rank 8 is at board[0], rank 1 at board[7]
        line = f"{rank}| "
        for col in range(8):
            piece = board[row][col]
            line += piece_to_symbol(piece) + " "
        print(line)
    print("   A B C D E F G H")
    print("=================================\n")
