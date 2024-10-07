import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkf
from PIL.ImageTk import PhotoImage
from typing import Callable, Literal, TypeVar


_T = TypeVar('_T')


class Button(tk.Canvas):
    _text_cf_items = {'text_color', 'font'}
    _canv_cf_items = {'cursor'}

    def __init__(self,
                 parent: tk.Misc,
                 width: int | None=None,
                 height: int | None=None,
                 ipadx: int=10,
                 ipady: int=10,
                 text: str='',
                 text_color: str | None=None,
                 background: str | None=None,
                 hover_background: str | None=None,
                 hover_text_color: str | None=None,
                 active_background: str | None=None,
                 active_text_color: str | None=None,
                 border_color: str | None=None,
                 border_radius: int=0,
                 image: PhotoImage | None=None,
                 style: str | None=None,
                 command: Callable[[tk.Event | None], None] | None=None,
                 font: tuple | tkf.Font | None=None,
                 cursor: str | None=None,
                 compound: Literal['top', 'bottom', 'left', 'right', 'center']=tk.TOP,
                 compound_padding: int=0,
                 justify: Literal['left', 'right', 'center']=tk.CENTER,
                 align: Literal['top', 'bottom', 'center']=tk.CENTER):
        super().__init__(parent,
                         borderwidth=0,
                         relief=tk.FLAT,
                         highlightthickness=0,
                         bg=background)

        self.parent = parent
        self._style = style
        self._command = command
        self._def_font = tkf.Font(size=10, family='Helvetica')
        self._font = font or self._def_font
        self._text = text
        self._image = image
        self._bg = background or self._get_style('background', 'light grey')
        self._fg = text_color or self._get_style('foreground', 'black')
        self._border_color = border_color or self._bg
        self._hover_bg = hover_background or self._get_style('highlightbackground', self._bg)
        self._hover_fg = hover_text_color or self._get_style('highlightcolor', self._fg)
        self._active_bg = active_background or self._get_style('activebackground', self._bg)
        self._active_fg = active_text_color or self._get_style('activeforeground', self._fg)
        self._cursor = cursor or self._get_style('cursor', 'hand2')
        self._compound = compound
        self._compound_padding = compound_padding
        self._ipadx = ipadx
        self._ipady = ipady
        self._justify = justify
        self._align = align
        self._state: Literal['active', 'normal', 'disabled', 'hovered'] = 'normal'
        self._def_state: Literal['active', 'normal', 'disabled', 'hovered'] = 'normal'

        # calculate dimensions
        text_height = self._font.metrics('linespace')
        min_height = text_height
        text_width = self._font.measure(self._text)
        min_width = text_width
        if self._image is not None:
            if self._compound == tk.LEFT or self._compound == tk.RIGHT:
                min_width = text_width + self._image.width()
                min_width += self._compound_padding
            else:
                min_width = max(min_width, self._image.width())

            if self._compound == tk.TOP or self._compound == tk.BOTTOM:
                min_height = text_height + self._image.height()
                min_height += self._compound_padding
            else:
                min_height = max(min_height, self._image.height())

        self._height = height or text_height
        if self._height < min_height:
            self._height = min_height

        self._height += self._ipady * 2
        
        self._width = width or min_width
        if self._width < min_width:
            self._width = min_width

        self._width += self._ipadx * 2

        # adjust border radius to not exceed dimensions
        if width is not None and height is not None:
            _limit = min(width, height)
            if border_radius > _limit * 0.5:
                border_radius = _limit * 0.5
        elif width is not None and border_radius > width * 0.5:
            border_radius = width * 0.5
        elif height is not None and border_radius > height * 0.5:
            border_radius = height * 0.5

        self._border_radius = border_radius

        _bg = self._bg
        _bc = border_color or _bg
        _rad = border_radius * 2
        def shape() -> int:
            _width = self._width
            _height = self._height
            self.create_arc((0, _rad, _rad, 0),
                            start=90,
                            extent=90,
                            fill=_bg,
                            outline=_bc)

            self.create_arc((_width - _rad, 0, _width, _rad),
                            start=0,
                            extent=90,
                            fill=_bg,
                            outline=_bc)

            self.create_arc((_width, _height - _rad, _width - _rad, _height),
                            start=270,
                            extent=90,
                            fill=_bg,
                            outline=_bc)

            self.create_arc((0, _height - _rad, _rad, _height),
                            start=180,
                            extent=90,
                            fill=_bg,
                            outline=_bc)

            return self.create_polygon((0, _height - border_radius, 0,
                                        border_radius, border_radius, 0,
                                        _width - border_radius, 0, _width,
                                        border_radius, _width,
                                        _height - border_radius,
                                        _width - border_radius,
                                        _height, border_radius, _height),
                                       fill=_bg,
                                       outline='black')

        self._id = shape()
        (x0, y0, x1, y1) = self.bbox('all')
        _width = x1 - x0
        _height = y1 - y0
        # self.configure(width=width, height=height)

        self._text_id: int | None = None
        self._image_id: int | None = None
        if self._image is not None:
            img_height = self._image.height()
            img_width = self._image.width()
            img_x = 0
            img_y = 0
            txt_x = 0
            txt_y = 0
            match self._compound:
                case tk.LEFT:
                    img_x = self._ipadx
                    img_y = self._ipady
                    if self._justify == tk.RIGHT:
                        txt_x = _width - self._ipady - text_width
                    elif self._justify == tk.LEFT:
                        txt_x = img_x + img_width + self._compound_padding
                    elif self._justify == tk.CENTER:
                        rem_width = _width - img_width - self._compound_padding
                        txt_x = rem_width // 2 - 1 + img_x + img_width + self._compound_padding
                    else:
                        raise tk.TclError(f'Invalid justify: {self._justify}')

                    if self._align == tk.TOP:
                        txt_y = _height - self._ipady
                    elif self._align == tk.BOTTOM:
                        txt_y = self._ipady
                    elif self._align == tk.CENTER:
                        txt_y = _height // 2 - 1
                    else:
                        raise tk.TclError(f'Invalid align: {self._align}')

                case tk.RIGHT:
                    img_x = _width - self._ipadx - img_width
                    img_y = self._ipady
                    if self._justify == tk.RIGHT:
                        txt_x = img_x - self._compound_padding - text_width
                    elif self._justify == tk.LEFT:
                        txt_x = self._ipadx
                    elif self._justify == tk.CENTER:
                        rem_width = _width - img_width - self._compound_padding
                        txt_x = rem_width // 2 - 1
                    else:
                        raise tk.TclError(f'Invalid justify: {self._justify}')

                    if self._align == tk.TOP:
                        txt_y = _height - self._ipady
                    elif self._align == tk.BOTTOM:
                        txt_y = self._ipady
                    elif self._align == tk.CENTER:
                        txt_y = _height // 2 - 1
                    else:
                        raise tk.TclError(f'Invalid align: {self._align}')

                case tk.TOP:
                    img_x = _width // 2 - img_width // 2
                    img_y = self._ipady
                    if self._justify == tk.RIGHT:
                        txt_x = _width - self._ipadx - text_width
                    elif self._justify == tk.LEFT:
                        txt_x = self._ipadx
                    elif self._justify == tk.CENTER:
                        txt_x = _width // 2 - 1
                    else:
                        raise tk.TclError(f'Invalid justify: {self._justify}')

                    if self._align == tk.TOP:
                        txt_y = img_y - self._compound_padding - text_height
                    elif self._align == tk.BOTTOM:
                        txt_y = self._ipady
                    elif self._align == tk.CENTER:
                        rem_height = _height - img_height - self._compound_padding
                        txt_y = rem_height // 2 - 1 + img_height + self._compound_padding
                    else:
                        raise tk.TclError(f'Invalid align: {self._align}')

                case tk.BOTTOM:
                    img_x = self._ipadx
                    img_y = self._ipady
                    if self._justify == tk.RIGHT:
                        txt_x = _width - self._ipadx - text_width
                    elif self._justify == tk.LEFT:
                        txt_x = self._ipadx
                    elif self._justify == tk.CENTER:
                        txt_x = _width // 2 - 1
                    else:
                        raise tk.TclError(f'Invalid justify: {self._justify}')

                    if self._align == tk.TOP:
                        txt_y = _height - self._ipady
                    elif self._align == tk.BOTTOM:
                        txt_y = img_x + img_height + self._compound_padding
                    elif self._align == tk.CENTER:
                        rem_height = _height - img_height - self._compound_padding
                        txt_y = rem_height // 2 - 1 + img_y + img_height + self._compound_padding
                    else:
                        raise tk.TclError(f'Invalid align: {self._align}')

                case tk.CENTER:
                    raise tk.TclError('Center is not currently implemented')

                case other:
                    raise tk.TclError(f'Invalid compund: {other}')

            self._image_id = self.create_image(img_x,
                                               img_y,
                                               anchor=tk.NW,
                                               image=self._image)
            self._text_id = self.create_text(txt_x,
                                             txt_y,
                                             text=self._text,
                                             fill=self._fg,
                                             font=self._font)

            self.tag_bind(self._image_id, '<ButtonPress-1>', self._on_press)
            self.tag_bind(self._image_id, '<ButtonRelease-1>', self._on_release)
        else:
            # TODO: add justification and alignment for pure text
            self._text_id = self.create_text(_width // 2 - 1,
                                             _height // 2 - 1,
                                             text=self._text,
                                             fill=self._fg,
                                             font=self._font)

        self.tag_bind(self._id, '<ButtonPress-1>', self._on_press)
        self.tag_bind(self._id, '<ButtonRelease-1>', self._on_release)
        self.tag_bind(self._id, '<Enter>', self._on_enter)
        self.tag_bind(self._id, '<Leave>', self._on_leave)
        self.tag_bind(self._text_id, '<ButtonPress-1>', self._on_press)
        self.tag_bind(self._text_id, '<ButtonRelease-1>', self._on_release)

    def _on_press(self, event: tk.Event) -> None:
        if self._state == 'disabled':
            return

        self.itemconfigure(self._id, fill=self._active_bg)

    def _on_release(self, event: tk.Event) -> None:
        if self._state == 'disabled':
            return

        x = self.winfo_rootx()
        y = self.winfo_rooty()
        if (event.x_root >= x
                and event.x_root <= self._width
                and event.y_root >= y
                and event.y_root <= self._height):
            self.itemconfigure(self._id, fill=self._hover_bg)
            self.itemconfigure(self._text_id, fill=self._hover_fg)
            self._state = 'hovered'
        else:
            self.itemconfigure(self._id, fill=self._bg)
            self.itemconfigure(self._text_id, fill=self._fg)
            self._state = 'normal'

        if self._command is not None:
            try:
                self._command(event)
            except TypeError:
                self._command()

    def _on_enter(self, event: tk.Event) -> None:
        if self._state == 'hovered' or self._state == 'disabled':
            return

        self.itemconfigure(self._id, fill=self._hover_bg)
        self.itemconfigure(self._text_id, fill=self._hover_fg)
        self.configure(cursor=self._cursor)
        self._state = 'hovered'

    def _on_leave(self, event: tk.Event) -> None:
        if self._state == 'disabled':
            return

        x = self.winfo_rootx()
        y = self.winfo_rooty()
        if (event.x_root >= x
                and event.x_root <= x + self._width
                and event.y_root >= y
                and event.y_root <= y + self._height):
            return

        self.itemconfigure(self._id, fill=self._bg)
        self.itemconfigure(self._text_id, fill=self._fg)
        self.configure(cursor='arrow')
        self._state = self._def_state

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

    def _text_configure(self, **kw) -> None:
        _kw = {}
        for key, value in kw.items():
            match key:
                case 'text_color':
                    _kw['fill'] = value
                case _:
                    _kw[key] = value

        self.itemconfigure(self._text_id, **_kw)

    def _btn_configure(self, **kw) -> None:
        if 'command' in kw:
            self._command = kw['command']
            del kw['command']

        self.itemconfigure(self._id, **kw)

    def configure(self, **kw) -> None:
        _text_kw = {}
        _btn_kw = {}
        _canv_kw = {}
        for key, value in kw.items():
            if key in self._text_cf_items:
                _text_kw[key] = value
            elif key in self._canv_cf_items:
                _canv_kw[key] = value
            else:
                _btn_kw[key] = value

        if _text_kw != {}:
            self._text_configure(**_text_kw)

        if _btn_kw != {}:
            self._btn_configure(**_btn_kw)

        if _canv_kw != {}:
            super().configure(**_canv_kw)
