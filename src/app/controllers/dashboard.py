import tkinter as tk

from src.app.views import View
from src.app.models import Model


class DashboardController:
    def __init__(self, model: Model, view: View):
        self.root_model = model
        self.root_view = view
        self.view = view.dashboard

        self._bind_navigation()

    def _show_parser_view(self, event: tk.Event | None=None) -> None:
        self.root_view.parser.show()
        self.root_view.app.set_nav('parser')

    def _show_summarizer_view(self, event: tk.Event | None=None) -> None:
        self.root_view.summarizer.show()
        self.root_view.app.set_nav('summarizer')

    def _show_perm_qa_qc_view(self, event: tk.Event | None=None) -> None:
        self.root_view.perm_qa_qc.show()
        self.root_view.app.set_nav('perm_qa_qc')

    def _bind_navigation(self) -> None:
        self.view.parser_btn.configure(command=self._show_parser_view)
        self.view.summarizer_btn.configure(command=self._show_summarizer_view)
        self.view.perm_qa_qc_btn.configure(command=self._show_perm_qa_qc_view)
