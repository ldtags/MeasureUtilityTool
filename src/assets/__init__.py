import os
from PIL import ImageTk, Image


_PATH = os.path.abspath(os.path.dirname(__file__))


def get_path(file_name: str, exists: bool=True) -> str:
    """Returns an absolute path to an asset file."""

    file_path = os.path.join(_PATH, file_name)
    if not os.path.exists(file_path) and exists:
        raise FileNotFoundError(f'No asset named {file_name} exists')

    return file_path


_IMAGES: dict[str, Image.Image] = {}
"""Cache for PIL images."""


def get_image(file_name: str) -> Image.Image:
    file_path = get_path(file_name)
    try:
        image = _IMAGES[file_path]
    except KeyError:
        image = Image.open(file_path)
        _IMAGES[file_path] = image

    return image


_TK_IMAGES: dict[str, ImageTk.PhotoImage] = {}
"""Cache for Tkinter images."""


def get_tkimage(file_name: str,
                size: tuple[int, int] | None=None
               ) -> ImageTk.PhotoImage:
    """Returns an image asset that can be used in a tkinter widget."""

    file_path = get_path(file_name)
    key = f'{file_path}{str(size)}'
    try:
        tk_image = _TK_IMAGES[key]
    except KeyError:
        image = Image.open(file_path)
        if size is not None:
            image = image.resize(size)
        tk_image = ImageTk.PhotoImage(image)
        _TK_IMAGES[key] = tk_image

    return tk_image
