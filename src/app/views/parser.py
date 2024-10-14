import tkinter as tk
import tkinter.ttk as ttk

from src.app.views.components import MeasureSelectionFrame
from src.app.widgets import Page


class ParserView(Page):
    def __init__(self, parent: ttk.Frame, **kw):
        super().__init__(parent, style='Page.TFrame', **kw)

        self.grid_rowconfigure((0, 4), weight=1)
        self.grid_rowconfigure((1, 2, 3), weight=0)
        self.grid_columnconfigure((0, 2), weight=2, uniform='ParserSpacing')
        self.grid_columnconfigure((1), weight=1)

        title_label = ttk.Label(self,
                                text='Select a Measure to Parse',
                                style='Header.Section.TLabel')
        title_label.grid(row=1,
                         column=1,
                         sticky=tk.NSEW,
                         pady=(0, 5))

        self.measure_frame = MeasureSelectionFrame(self,
                                                   file_text='Select an eTRM Measure JSON File',
                                                   etrm_text='Enter an eTRM Measure Version ID',
                                                   btn_text='Parse Measure')
        self.measure_frame.grid(row=2,
                                column=1,
                                sticky=tk.NSEW)

    @property
    def key(self) -> str:
        return 'parser'

    def show(self) -> None:
        self.tkraise()

