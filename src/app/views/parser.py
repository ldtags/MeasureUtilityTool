import tkinter as tk
import tkinter.ttk as ttk

from src.app.widgets import Page


class ParserView(Page):
    def __init__(self, parent: ttk.Frame, **kwargs):
        super().__init__(parent, style='Parser.TFrame', **kwargs)

    @property
    def key(self) -> str:
        return 'parser'

    def show(self) -> None:
        self.tkraise()
