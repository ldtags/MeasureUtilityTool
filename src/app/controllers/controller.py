from src.app.views import View, DashboardView
from src.app.models import Model
from src.app.controllers.dashboard import DashboardController


class Controller:
    def __init__(self):
        self.model = model = Model()
        self.view = view = View()
        self.dashboard = DashboardController(model, view)

    def start(self) -> None:
        self.view.show(DashboardView)
        self.view.start()
