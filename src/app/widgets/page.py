import tkinter as tk
import tkinter.ttk as ttk
from abc import ABCMeta, abstractmethod
from typing import TypeVar as _TypeVar

from src.app.widgets.frame import Frame


class Page(Frame, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, parent: ttk.Frame, padx: int=0, pady: int=0, **kwargs):
        if self.__class__ == Page:
            raise Exception('Cannot instantiate an abstract base class')

        super().__init__(parent, **kwargs)
        self.grid(row=0,
                  column=0,
                  sticky=tk.NSEW)

    @abstractmethod
    def show(self) -> None:
        ...


PageType = _TypeVar('PageType', bound=Page)
