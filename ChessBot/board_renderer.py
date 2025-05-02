import os

from PIL import Image

from chess_setups import Piece

# get location of assets
running_dir = os.path.dirname(os.path.realpath(__file__))
assets_dir = str(running_dir) + "\\assets\\"
output_dir = str(running_dir) + "\\output\\"

print(assets_dir)


def piece_to_filename(piece: Piece) -> str:
    if piece == Piece.NULL:
        return None
    color = 'white' if piece.color.name == 'WHITE' else 'black'
    name = piece.type.name.lower()
    return f'pieces\\{color}-{name}.png'


def draw_board(board_data):
    board_image = os.path.join(assets_dir, "boards\\board_8x8.png")

    # open image
    board_img = Image.open(board_image).convert("RGBA")

    # Size of one square (board is 8x8 squares)
    square_size = board_img.width // 8

    for idx, piece in enumerate(board_data.square):
        if piece == Piece.NULL:
            continue

        row = idx // 8
        col = idx % 8

        piece_path = piece_to_filename(piece)
        if not piece_path:
            continue

        piece_img_path = os.path.join(assets_dir, piece_path)

        piece_img = Image.open(piece_img_path).convert("RGBA")
        piece_img = piece_img.resize((square_size, square_size))
        x, y = col * square_size, row * square_size
        board_img.paste(piece_img, (x, y), piece_img)

    board_img.save(os.path.join(output_dir, "board_new.png"))
    # board_img.show()  # Optional: display with default image viewer

