import os
import math
import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image as ImageModule
from PIL.Image import Image, Resampling
from PIL.ImageFile import ImageFile
from typing import Literal, overload


_PATH = os.path.abspath(os.path.dirname(__file__))


def get_path(file_name: str, exists: bool=True) -> str:
    """Returns an absolute path to an asset file."""

    file_path = os.path.join(_PATH, file_name)
    if not os.path.exists(file_path) and exists:
        raise FileNotFoundError(f'No asset named {file_name} exists')

    return file_path


_IMAGES: dict[str, Image] = {}
"""Cache for PIL images."""


def get_image(file_name: str) -> Image:
    file_path = get_path(file_name)
    try:
        image = _IMAGES[file_path]
    except KeyError:
        image = ImageModule.open(file_path)
        _IMAGES[file_path] = image

    return image


_TK_IMAGES: dict[str, ImageTk.PhotoImage] = {}
"""Cache for Tkinter images."""


@overload
def resize_image(image: ImageFile,
                 size: int,
                 relative: Literal['height', 'width']
                ) -> Image:
    ...


@overload
def resize_image(image: ImageFile,
                 size: tuple[int, int]
                ) -> Image:
    ...


def resize_image(image: ImageFile,
                 size: tuple[int, int] | int,
                 relative: Literal['height', 'width'] | None=None
                ) -> Image:
    """Resizes an image to fit in the dimensions specified by `size`.

    Maintains the original aspect ratio of the image (no cropping).

    Returns the largest image possible.
    """

    if isinstance(size, int) and relative is None:
        raise RuntimeError('No relative dimension specified')

    if isinstance(size, tuple) and relative is not None:
        raise RuntimeError('Relative dimension size must be an integer')

    if isinstance(size, tuple):
        max_width = size[0]
        max_height = size[1]
    else:
        max_width = size
        max_height = size

    # calcuate image dimensions and size relative to width
    aspect_ratio_w = image.width / image.height
    img_width_w = math.floor(max_width * aspect_ratio_w)
    total_size_w = max_height * img_width_w

    # calculate image dimensions and size relative to height
    aspect_ratio_h = image.height / image.width
    img_height_h = math.floor(max_height * aspect_ratio_h)
    total_size_h = img_height_h * max_width

    new_size: tuple[int, int] | None = None
    match relative:
        case 'height':
            new_size = (img_width_w, size)
        case 'width':
            new_size = (size, img_height_h)
        case None:
            if total_size_w > total_size_h:
                new_size = (img_width_w, max_height)
            else:
                new_size = (max_width, img_height_h)
        case other:
            raise RuntimeError(f'Invalid dimension: {other}')

    return image.resize(new_size, Resampling.LANCZOS)


def get_tkimage(file_name: str,
                size: tuple[int, int] | int | None=None,
                relative: Literal['width', 'height'] | None=None,
                parent: tk.Misc | None=None
               ) -> ImageTk.PhotoImage:
    """Returns an image asset that can be used in a tkinter widget.

    `size` is a 2-tuple defined by (width, height).
    """

    file_path = get_path(file_name)
    key = f'{file_path}{str(size)}'
    try:
        tk_image = _TK_IMAGES[key]
    except KeyError:
        image = ImageModule.open(file_path)
        if size is not None:
            image = resize_image(image, size, relative)
        tk_image = ImageTk.PhotoImage(master=parent, image=image)
        _TK_IMAGES[key] = tk_image

    return tk_image


def get_ctkimage(light_image: str | None=None,
                 dark_image: str | None=None,
                 size: tuple[int, int]=(20, 20)
                ) -> ctk.CTkImage:
    if light_image is None and dark_image is None:
        raise tk.TclError('No image path provided')

    if light_image is not None:
        light_path = get_path(light_image)
    else:
        light_path = None

    if dark_image is not None:
        dark_path = get_path(dark_image)
    else:
        dark_path = None

    light_path = light_path or dark_path
    dark_path = dark_path or light_path
    return ctk.CTkImage(light_image=ImageModule.open(light_path),
                        dark_image=ImageModule.open(dark_path),
                        size=size)
