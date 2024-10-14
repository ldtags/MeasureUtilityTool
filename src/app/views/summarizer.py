import tkinter as tk
import tkinter.ttk as ttk

from src.app.widgets import Page, ScrollableFrame
from src.app.views.components import MeasureSelectionFrame


class SummarizerView(Page):
    def __init__(self, parent: ttk.Frame, **kwargs):
        super().__init__(parent, style='Summarizer.TFrame', **kwargs)

        self.grid_rowconfigure((0, 4), weight=1)
        self.grid_rowconfigure((1, 2, 3), weight=0)
        self.grid_columnconfigure((0, 2, 4), weight=1, uniform='SummarizerSpacing')
        self.grid_columnconfigure((1, 3), weight=3, uniform='SummarizerItems')

        measure_label = ttk.Label(self, text='Select Measures to Summarize', style='Header.Section.TLabel')
        measure_label.grid(row=1,
                           column=1,
                           sticky=tk.SW,
                           pady=(0, 5))

        self.measure_frame = MeasureSelectionFrame(self,
                                                   file_text='Select an eTRM Measure JSON File',
                                                   etrm_text='Enter an eTRM Measure Version ID or Use Category',
                                                   btn_text='Add Measure(s)')
        self.measure_frame.grid(row=2,
                                column=1,
                                sticky=tk.NSEW)

        selection_label = ttk.Label(self, text='Selected Measures', style='Header.Section.TLabel')
        selection_label.grid(row=1,
                             column=3,
                             sticky=tk.SW,
                             pady=(0, 5))

        self.selection_frame = ScrollableFrame(self)
        self.selection_frame.grid(row=2,
                                  column=3,
                                  sticky=tk.NSEW)

        self.start_btn = ttk.Button(self, text='Summarize Measure(s)', cursor='hand2')
        self.start_btn.grid(row=3,
                            column=3,
                            sticky=tk.SE,
                            padx=(10, 10),
                            pady=(10, 0),
                            ipadx=8)

    @property
    def key(self) -> str:
        return 'summarizer'

    def show(self) -> None:
        self.tkraise()
