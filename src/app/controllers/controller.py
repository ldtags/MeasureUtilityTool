from src.app.views import View, DashboardView
from src.app.models import Model
from src.app.controllers.app import AppController
from src.app.controllers.dashboard import DashboardController
from src.app.controllers.parser import ParserController
from src.app.controllers.summary import SummaryController
from src.app.controllers.perm_qa_qc import PermQaQcController
from src.app.controllers.progress import ProgressController


class Controller:
    def __init__(self):
        self.model = model = Model()
        self.view = view = View()
        self.app = AppController(model, view)
        self.dashboard = DashboardController(model, view)
        self.parser = ParserController(model, view)
        self.summary = SummaryController(model, view)
        self.perm_qa_qc = PermQaQcController(model, view)
        self.progress = ProgressController(model, view)

    def start(self) -> None:
        self.view.show(DashboardView)
        self.view.start()
