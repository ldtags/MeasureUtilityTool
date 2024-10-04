import tkinter as tk
import tkinter.ttk as ttk

from src.app.widgets import Page


class PermQaQcView(Page):
    def __init__(self, parent: ttk.Frame, **kwargs):
        super().__init__(parent, style='PermQaQc.TFrame', **kwargs)

    @property
    def key(self) -> str:
        return 'perm_qa_qc'

    def show(self) -> None:
        self.tkraise()