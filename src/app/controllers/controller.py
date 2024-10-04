import tkinter as tk
import tkinter.ttk as ttk

from src.app.views import View, DashboardView
from src.app.models import Model
from src.app.controllers.app import AppController
from src.app.controllers.dashboard import DashboardController


class Controller:
    def __init__(self):
        self.model = model = Model()
        self.view = view = View()
        self.app = AppController(model, view)
        self.dashboard = DashboardController(model, view)

        self._set_styles()

    def start(self) -> None:
        self.view.show(DashboardView)
        self.view.start()

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
            cursor='hand2'
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
