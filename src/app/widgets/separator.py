import tkinter as tk
import tkinter.ttk as ttk
from typing import Literal, TypeVar

from src.app.widgets import Frame


_T = TypeVar('_T')


class Separator(tk.Frame):
    def __init__(self,
                 parent: tk.Misc,
                 width: int=1,
                 orient: Literal['horizontal', 'vertical']='horizontal',
                 color: str | None=None,
                 style: str | None=None):
        self._color = color or 'black'
        self._style = style

        bg = self._get_style('background', self._color)

        _height = None
        _width = None
        match orient:
            case 'horizontal':
                _height = width
            case 'vertical':
                _width = width

        super().__init__(parent, background=bg, height=_height, width=_width, bd=0)

    def _get_style(self, option: str, default: _T, state: str | None=None) -> _T:
        if self._style is None:
            return default

        style = ttk.Style()
        style_name = f'{self._style}'
        while '.' in style_name:
            style_value = style.lookup(self._style, option, state, None)
            if style_value is not None and style_value != '':
                return style_value

            style_name = style_name[style_name.index('.') + 1:]

        style_value = style.lookup(self._style, option, state, default)
        if style_value == '':
            return default

        return style_value


class MutexSeparator(Frame):
    def __init__(self,
                 parent: Frame,
                 orient: Literal['horizontal', 'vertical']='horizontal',
                 style: str | None=None,
                 sep_style: str | None=None,
                 **kwargs):
        super().__init__(parent, style=parent.style, **kwargs)

        self._style = style
        self._sep_style = sep_style

        match orient:
            case 'horizontal':
                self._horizontal_init()
            case 'vertical':
                self._vertical_init()
            case other:
                raise tk.TclError(f'Invalid orient: {other}')

    def _horizontal_init(self) -> None:
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_columnconfigure((1), weight=0)

        left_sep = ttk.Separator(self, style=self._sep_style)
        left_sep.grid(row=0,
                      column=0,
                      sticky=tk.EW)

        label = ttk.Label(self, style=self._style, text='OR')
        label.grid(row=0,
                   column=1,
                   sticky=tk.NSEW)

        right_sep = ttk.Separator(self, style=self._sep_style)
        right_sep.grid(row=0,
                       column=2,
                       sticky=tk.EW)

    def _vertical_init(self) -> None:
        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure((1), weight=0)
        self.grid_columnconfigure((0), weight=1)

        top_sep = ttk.Separator(self, style=self._sep_style)
        top_sep.grid(row=0,
                     column=0,
                     sticky=tk.NS)

        label = ttk.Label(self, style=self._style, text='OR')
        label.grid(row=1,
                   column=0,
                   sticky=tk.NSEW)

        bottom_sep = ttk.Separator(self, style=self._sep_style)
        bottom_sep.grid(row=2,
                        column=0,
                        sticky=tk.NS)
