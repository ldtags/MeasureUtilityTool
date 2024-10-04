import tkinter as tk
import tkinter.ttk as ttk

from src.app.widgets import Page


class SummarizerView(Page):
    def __init__(self, parent: ttk.Frame, **kwargs):
        super().__init__(parent, style='Summarizer.TFrame', **kwargs)

    @property
    def key(self) -> str:
        return 'summarizer'

    def show(self) -> None:
        self.tkraise()