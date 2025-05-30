import os

from PIL import Image

from pieces import Piece
from debug_outputting import print_board_debug


# get location of assets
running_dir = os.path.dirname(os.path.realpath(__file__))
assets_dir = str(running_dir) + "\\assets\\"
output_dir = str(running_dir) + "\\output\\"


def piece_to_filename(piece: Piece) -> str:
    if piece == Piece.NULL:
        return f'pieces\\ERROR.png'
    color = 'white' if piece.color.name == 'WHITE' else 'black'
    name = piece.type.name.lower()
    return f'pieces\\{color}-{name}.png'


def draw_board(board_data):
    board_image = os.path.join(assets_dir, "boards\\board_8x8.png")

    # open image
    board_img = Image.open(board_image).convert("RGBA")

    # Size of one square (board is 8x8 squares)
    board_scale = 8

    square_size = board_img.width // board_scale

    for row in range(board_scale):
        for col in range(board_scale):
            piece = board_data.squares[row][col]
            if piece == Piece.NULL:
                continue

            piece_path = piece_to_filename(piece)
            if not piece_path:
                continue

            piece_img_path = os.path.join(assets_dir, piece_path)

            piece_img = Image.open(piece_img_path).convert("RGBA")
            piece_img = piece_img.resize((square_size, square_size))
            x = col * square_size
            y = row * square_size  # Flip to `7 - row` if board image has rank 1 at the bottom
            board_img.paste(piece_img, (x, y), piece_img)

    # save new image of board
    board_img.save(os.path.join(output_dir, "board_new.png"))
    # Print board to console
    print_board_debug(board_data.squares)
