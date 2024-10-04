import tkinter as tk

from src.app.views import View
from src.app.models import Model


class AppController:
    def __init__(self, model: Model, view: View):
        self.root_model = model
        self.root_view = view
        self.view = view.app

        self._bind_navigation()

    def _show_dash_view(self, event: tk.Event | None=None) -> None:
        self.root_view.dashboard.show()

    def _show_parser_view(self, event: tk.Event | None=None) -> None:
        self.root_view.parser.show()

    def _show_summarizer_view(self, event: tk.Event | None=None) -> None:
        self.root_view.summarizer.show()

    def _show_perm_qa_qc_view(self, event: tk.Event | None=None) -> None:
        self.root_view.perm_qa_qc.show()

    def _bind_navigation(self) -> None:
        navbar = self.view.navbar.navbar_list
        navbar.dashboard_item.set_event(self._show_dash_view)
        navbar.parser_item.set_event(self._show_parser_view)
        navbar.summarizer_item.set_event(self._show_summarizer_view)
        navbar.perm_qa_qc_item.set_event(self._show_perm_qa_qc_view)
