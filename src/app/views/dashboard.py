import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk

from src import assets
from src.app import utils
from src.app.widgets import Page


class DashboardView(Page):
    def __init__(self, parent: ttk.Frame, **kwargs):
        super().__init__(parent, style='Dashboard.TFrame', **kwargs)

        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure((1), weight=0)
        self.grid_columnconfigure((0, 2, 4, 6), weight=1)
        self.grid_columnconfigure((1, 3, 5), weight=0)

        parent_height = parent.winfo_height()
        parent_width = parent.winfo_width()
        btn_size = (parent_height // 3 - 40, parent_width // 5 - 40)

        self.parser_btn = DashboardButton(self, 'Parse a Measure', 'square-document.png', btn_size)
        self.parser_btn.grid(row=1,
                             column=1,
                             sticky=tk.NSEW,
                             ipady=8)

        self.summarizer_btn = DashboardButton(self, 'Summarize a Measure', 'pdf-black.png', btn_size)
        self.summarizer_btn.grid(row=1,
                                 column=3,
                                 sticky=tk.NSEW,
                                 ipady=8)

        self.perm_qa_qc_btn = DashboardButton(self, 'QA/QC Permutations', 'square-document.png', btn_size)
        self.perm_qa_qc_btn.grid(row=1,
                                 column=5,
                                 sticky=tk.NSEW,
                                 ipady=8)

    @property
    def key(self) -> str:
        return 'dashboard'

    def show(self) -> None:
        self.tkraise()


class DashboardButton(ctk.CTkButton):
    def __init__(self,
                 parent: DashboardView,
                 text: str,
                 image: str,
                 img_size: tuple[int, int],
                 style='Dashboard.Option.TButton',
                 **kw):
        bg = utils.get_style(style, 'background', 'transparent')
        text_color = utils.get_style(style, 'foreground', '#000000')
        hover_color = utils.get_style(style, 'highlightbackground', 'transparent')
        border_color = utils.get_style(style, 'bordercolor', 'transparent')
        super().__init__(parent,
                         text=text,
                         compound=tk.TOP,
                         image=assets.get_ctkimage(image, size=img_size),
                         fg_color=bg,
                         text_color=text_color,
                         border_width=2,
                         border_color=border_color,
                         hover_color=hover_color,
                         **kw)
