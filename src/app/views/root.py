import os
import tkinter as tk
import tkinter.ttk as ttk
from ctypes import windll

from src import assets


# fixes blurry text on Windows 10
if os.name == 'nt':
    windll.shcore.SetProcessDpiAwareness(1)


class Root(tk.Tk):
    def __init__(self, width: int=1500, height: int=850):
        super().__init__()

        self.title('eTRM Measure Utility Tool')
        self.iconbitmap(assets.get_path('app.ico'))
        self.geometry(f'{width}x{height}')
        self.minsize(width=width, height=height)
        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure((0), weight=1)

        self.container = ttk.Frame(self)
        self.container.grid(row=0, column=0, sticky=tk.NSEW)
        self.container.grid_rowconfigure((0), weight=1)
        self.container.grid_columnconfigure((0), weight=1)

        self._set_styles()

    def _set_frame_styles(self, style: ttk.Style) -> None:
        style.configure(
            'Frame',
            background='#dfe2e7'
        )

        style.configure(
            'NavBar.TFrame',
            background='#6b6b6b',
            width=300
        )

        style.configure(
            'List.NavBar.TFrame'
        )

        style.configure(
            'Item.List.NavBar.TFrame',
            cursor='hand2'
        )

        style.configure(
            'Accent.Item.List.NavBar.TFrame',
            background='#6e9460'
        )

        style.configure(
            'Highlight.Item.List.NavBar.TFrame',
            background='#4e4e4e'
        )

        style.configure(
            'Highlight.Item.List.NavBar.TFrame',
            background='#4e4e4e'
        )

        style.configure(
            'Active.Item.List.NavBar.TFrame',
            background='#5c5c5c'
        )

        style.configure(
            'Footer.TFrame',
            background='#6b6b6b'
        )

    def _set_label_styles(self, style: ttk.Style) -> None:
        style.configure(
            'TLabel',
            font=('Segoe UI', 12)
        )

        style.configure(
            'NavBar.TLabel',
            background='#6b6b6b',
            foreground='#ffffff'
        )

        style.configure(
            'List.NavBar.TLabel',
            foreground='#ffffff',
            font=('Bahnschrift Light', 10, 'bold')
        )

        style.configure(
            'Highlight.List.NavBar.TLabel',
            background='#4e4e4e'
        )

        style.configure(
            'Active.List.NavBar.TLabel',
            background='#5c5c5c'
        )

        style.configure(
            'Icon.List.NavBar.TLabel'
        )

    def _set_button_styles(self, style: ttk.Style) -> None:
        style.configure(
            'TButton',
            font=('Segoe UI', 12),
            cursor='hand2'
        )

        style.configure(
            'Dashboard.Option.TButton',
            compound=tk.BOTTOM
        )

    def _set_styles(self) -> None:
        style = ttk.Style()
        self._set_frame_styles(style)
        self._set_label_styles(style)
