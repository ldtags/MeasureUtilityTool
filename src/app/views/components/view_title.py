import tkinter as tk
import tkinter.ttk as ttk

from src.app.widgets import Separator, Frame


class ViewTitle(Frame):
    def __init__(self, parent: Frame, text: str, **kw):
        super().__init__(parent, **kw)

        self.grid_rowconfigure((0, 1), weight=0)
        self.grid_columnconfigure((0), weight=0)

        title = ttk.Label(self, text=text, style='Title.View.TLabel')
        title.grid(row=0,
                   column=0,
                   sticky=tk.NSEW,
                   padx=(0, 10))

        sep = Separator(self)
        sep.grid(row=1,
                 column=0,
                 sticky=tk.EW)
