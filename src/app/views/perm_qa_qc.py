import tkinter as tk
import tkinter.ttk as ttk

from src.app.widgets import Page
from src.app.views.components import MeasureSelectionFrame


class PermQaQcView(Page):
    def __init__(self, parent: ttk.Frame, **kwargs):
        super().__init__(parent, style='Page.TFrame', **kwargs)

        self.grid_rowconfigure((0, 3), weight=2, uniform='PermQaQcSpacing')
        self.grid_rowconfigure((1), weight=0)
        self.grid_rowconfigure((2), weight=2)
        self.grid_columnconfigure((0, 2), weight=2, uniform='PermQaQcSpacing')
        self.grid_columnconfigure((1), weight=2)

        title_label = ttk.Label(self,
                                text='Select a Measure to QA/QC Permutations',
                                style='Header.Section.TLabel')
        title_label.grid(row=1,
                         column=1,
                         sticky=tk.NSEW,
                         pady=(0, 5))

        self.measure_frame = MeasureSelectionFrame(self,
                                                   file_text='Select an eTRM Measure Permutations CSV File',
                                                   file_types=('CSV Files', '*.csv'),
                                                   etrm_text='Enter an eTRM Measure Version ID',
                                                   btn_text='QA/QC Permutations')
        self.measure_frame.grid(row=2,
                                column=1,
                                sticky=tk.NSEW)

    @property
    def key(self) -> str:
        return 'perm_qa_qc'

    def show(self) -> None:
        self.tkraise()
