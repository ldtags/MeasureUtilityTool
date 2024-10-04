import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkf
from typing import Callable

from src import assets
from src.app.widgets import Page


class DashboardView(Page):
    def __init__(self, parent: ttk.Frame, **kwargs):
        super().__init__(parent, style='Dashboard.TFrame', **kwargs)

        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_columnconfigure((0, 2, 4, 6), weight=1)
        self.grid_propagate(False)

        parent_height = parent.winfo_height()
        parent_width = parent.winfo_width()
        btn_height = parent_height // 3
        btn_width = parent_width // 5

        self.parser_btn = DashboardButton(self,
                                          text='Parse a Measure',
                                          image='square-document.png',
                                          height=btn_height,
                                          width=btn_width)
        self.parser_btn.grid(row=1,
                             column=1,
                             sticky=tk.NSEW)

        self.summarizer_btn = DashboardButton(self,
                                              text='Summarize a Measure',
                                              image='pdf-black.png',
                                              height=btn_height,
                                              width=btn_width)
        self.summarizer_btn.grid(row=1,
                                 column=3,
                                 sticky=tk.NSEW)

        self.perm_qa_qc_btn = DashboardButton(self,
                                              text='QA/QC Permutations',
                                              image='square-document.png',
                                              height=btn_height,
                                              width=btn_width)
        self.perm_qa_qc_btn.grid(row=1,
                                 column=5,
                                 sticky=tk.NSEW)

    @property
    def key(self) -> str:
        return 'dashboard'

    def show(self) -> None:
        self.tkraise()


class DashboardButton(ttk.Frame):
    _FRAME_ATTRS = {'height', 'width'}

    def __init__(self,
                 parent: DashboardView,
                 text: str,
                 image: str,
                 height: int,
                 width: int,
                 style: str='Dashboard.Option.TButton',
                 command: Callable[[tk.Event | None], None] | None=None,
                 cursor='hand2',
                 **kwargs):
        super().__init__(parent, height=height, width=width)

        self.pack_propagate(False)
        label = ttk.Label(self, text=text)
        text_height = tkf.Font(font=label['font']).metrics('linespace')
        label.destroy()
        img_height = height - 50 - text_height
        img_width = width - 50
        self._image = assets.get_tkimage(image,
                                         (img_width, img_height),
                                         parent=self)
        self._btn = ttk.Button(self,
                               text=text,
                               image=self._image,
                               style=style,
                               command=command,
                               cursor=cursor,
                               padding=(20, 20),
                               **kwargs)
        self._btn.pack(fill=tk.BOTH, expand=True)

    def configure(self, **kwargs) -> None:
        frame_kwargs: dict[str,] = {}
        btn_kwargs: dict[str,] = {}

        for key, value in kwargs:
            if key in DashboardButton._FRAME_ATTRS:
                frame_kwargs[key] = value
            else:
                btn_kwargs[key] = value

        if frame_kwargs != {}:
            self.configure(**frame_kwargs)

        if btn_kwargs != {}:
            self._btn.configure(**btn_kwargs)
