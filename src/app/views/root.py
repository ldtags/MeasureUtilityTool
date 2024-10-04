import os
import tkinter as tk
import tkinter.ttk as ttk
from ctypes import windll

from src import assets
from src.app.views.app import App


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
