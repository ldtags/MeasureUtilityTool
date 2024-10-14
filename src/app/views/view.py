from src.app.views.app import App
from src.app.views.root import Root
from src.app.views.dashboard import DashboardView
from src.app.views.parser import ParserView
from src.app.views.summarizer import SummarizerView
from src.app.views.perm_qa_qc import PermQaQcView
from src.app.views.styles import set_styles
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
        set_styles()

        self.app = app = App(root.container)
        app.post_process()

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
