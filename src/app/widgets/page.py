import tkinter as tk
import tkinter.ttk as ttk
from abc import ABCMeta, abstractmethod
from typing import TypeVar as _TypeVar


class Page(ttk.Frame, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, parent: ttk.Frame, **kwargs):
        if self.__class__ == Page:
            raise Exception('Cannot instantiate an abstract base class')

        super().__init__(parent, **kwargs)
        self.grid(row=0, column=0, sticky=tk.NSEW)

        parent_height = parent.winfo_height()
        parent_width = parent.winfo_width()
        self.configure(height=parent_height,
                       width=parent_width)

    @abstractmethod
    def show(self) -> None:
        ...


PageType = _TypeVar('PageType', bound=Page)
