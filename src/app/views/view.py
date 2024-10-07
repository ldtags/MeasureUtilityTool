import tkinter as tk
import tkinter.ttk as ttk

from src.app.views.app import App
from src.app.views.root import Root
from src.app.views.dashboard import DashboardView
from src.app.views.parser import ParserView
from src.app.views.summarizer import SummarizerView
from src.app.views.perm_qa_qc import PermQaQcView
from src.app.widgets import Page, PageType
from src.app.exceptions import (
    GUIError
)


class View:
    """Top level view class for the MVC pattern.

    Controls all views of the application.
    """

    def __init__(self):
        self.root = root = Root()
        self.app = app = App(root.container)
        app.post_process()
        self._set_styles()

        self.dashboard = DashboardView(app.container)
        self.parser = ParserView(app.container)
        self.summarizer = SummarizerView(app.container)
        self.perm_qa_qc = PermQaQcView(app.container)

        self.pages: dict[PageType, Page] = {
            DashboardView: self.dashboard,
            ParserView: self.parser,
            SummarizerView: self.summarizer,
            PermQaQcView: self.perm_qa_qc
        }

    def show(self, page: PageType) -> None:
        try:
            self.pages[page].show()
        except KeyError:
            raise GUIError(f'Unknown page: {page}')

    def start(self) -> None:
        self.root.mainloop()

    def close(self) -> None:
        self.root.destroy()

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

        style.configure(
            'Dashboard.TFrame'
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
            cursor='hand2',
            background='#bfbfbf',
            foreground='#000000',
            activebackground='#8c8c8c',
            highlightbackground='#9d9d9d'
        )

        style.configure(
            'Dashboard.Option.TButton',
            compound=tk.TOP
        )

    def _set_styles(self) -> None:
        style = ttk.Style()
        self._set_frame_styles(style)
        self._set_label_styles(style)
        self._set_button_styles(style)

