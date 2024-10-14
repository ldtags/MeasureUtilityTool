import tkinter as tk

from src.app.widgets import Frame, ScrollableFrame


class ProgressFrame(Frame):
    def __init__(self, parent: Frame, **kw):
        super().__init__(parent, **kw)

        self.container = ScrollableFrame(self, background='#ffffff')
        self.container.pack(side=tk.TOP,
                            anchor=tk.NW,
                            fill=tk.BOTH,
                            expand=tk.TRUE)
