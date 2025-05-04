from board_data import ChessBoard
from board_renderer import draw_board

board = ChessBoard()
board.default_board_start()
# board.debug_board()

draw_board(board)
