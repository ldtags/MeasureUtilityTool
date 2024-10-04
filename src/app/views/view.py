from src.app.views.app import App
from src.app.views.root import Root
from src.app.views.dashboard import DashboardView
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

        self.dashboard = DashboardView(app.container)

        self.pages: dict[PageType, Page] = {
            DashboardView: self.dashboard
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
