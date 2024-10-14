import tkinter.ttk as ttk
from typing import TypeVar


_T = TypeVar('_T')


def get_style(style: str | None, option: str, default: _T | None, state: str | None=None) -> _T:
    if style is None:
        return default

    style_obj = ttk.Style()
    style_name = f'{style}'
    while '.' in style_name:
        style_value = style_obj.lookup(style, option, state, None)
        if style_value is not None and style_value != '':
            return style_value
        style_name = style_name[style_name.index('.') + 1:]

    style_value = style_obj.lookup(style, option, state, default)
    if style_value == '':
        return default

    return style_value
