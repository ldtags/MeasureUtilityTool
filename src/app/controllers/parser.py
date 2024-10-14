import tkinter as tk

from src.app.views import View
from src.app.models import Model


class ParserController:
    def __init__(self, model: Model, view: View):
        self.root_model = model
        self.root_view = view
        self.view = view.parser
