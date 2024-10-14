import tkinter as tk
import tkinter.ttk as ttk

from src.app.widgets import Frame, FileEntry, MutexSeparator


class MeasureSelectionFrame(Frame):
    def __init__(self,
                 parent: tk.Misc,
                 file_text: str,
                 etrm_text: str,
                 file_types: tuple[str, str] | list[tuple[str, str]] = ('JSON Files', '*.json'),
                 dialog_text: str='Select a File',
                 style: str='Form.TFrame',
                 **kwargs):
        super().__init__(parent, style=style, **kwargs)

        container = Frame(self, style='Form.TFrame')
        container.pack(side=tk.TOP,
                       anchor=tk.NW,
                       fill=tk.BOTH,
                       expand=tk.TRUE,
                       padx=(10, 10),
                       pady=(10, 10))

        container.grid_rowconfigure((1, 2, 3), weight=1)
        container.grid_rowconfigure((0), weight=0)
        container.grid_columnconfigure((0), weight=1)

        measure_selection_label = ttk.Label(container,
                                            text='Select a Measure',
                                            style='Header.Form.TLabel')
        measure_selection_label.grid(row=0,
                                     column=0,
                                     sticky=tk.NSEW)

        json_container = Frame(container, style=style)
        json_container.grid(row=1,
                            column=0,
                            sticky=tk.NSEW)

        json_container.grid_rowconfigure((0, 3), weight=1)
        json_container.grid_rowconfigure((1, 2), weight=0)
        json_container.grid_columnconfigure((0), weight=1)

        json_label = ttk.Label(json_container,
                               text=file_text,
                               style='Item.Form.TLabel')
        json_label.grid(row=1,
                        column=0,
                        sticky=tk.NW,
                        pady=(0, 2))

        self.json_entry = FileEntry(json_container,
                                    entry_style='Form.TEntry',
                                    file_types=file_types,
                                    dialog_text=dialog_text)
        self.json_entry.grid(row=2,
                             column=0,
                             sticky=tk.NSEW)

        separator = MutexSeparator(container,
                                   orient='horizontal',
                                   style='Item.Form.TLabel',
                                   sep_style='Form.TSeparator')
        separator.grid(row=2,
                       column=0,
                       sticky=tk.NSEW)

        etrm_container = Frame(container, style=style)
        etrm_container.grid(row=3,
                            column=0,
                            sticky=tk.NSEW)

        etrm_container.grid_rowconfigure((0, 7), weight=1)
        etrm_container.grid_rowconfigure((3), weight=2)
        etrm_container.grid_rowconfigure((1, 2, 4, 5, 6), weight=0)
        etrm_container.grid_columnconfigure((0), weight=1)

        etrm_label = ttk.Label(etrm_container,
                               style='Item.Form.TLabel',
                               text=etrm_text)
        etrm_label.grid(row=1,
                        column=0,
                        sticky=tk.NW,
                        pady=(0, 2))

        self.etrm_entry = ttk.Entry(etrm_container, style='Form.TEntry')
        self.etrm_entry.grid(row=2,
                             column=0,
                             sticky=tk.NSEW)

        key_label = ttk.Label(etrm_container,
                              style='Item.Form.TLabel',
                              text='Enter your eTRM API Key')
        key_label.grid(row=4,
                       column=0,
                       sticky=tk.NW,
                       pady=(0, 2))

        self.key_entry = ttk.Entry(etrm_container, style='Form.TEntry')
        self.key_entry.grid(row=5,
                            column=0,
                            sticky=tk.NSEW)

        self.rm_var = tk.IntVar(etrm_container, 0)
        self.rm_checkbox = ttk.Checkbutton(etrm_container,
                                           text='Remember Me',
                                           variable=self.rm_var,
                                           style='Form.TCheckbutton',
                                           cursor='hand2')
        self.rm_checkbox.grid(row=6,
                              column=0,
                              sticky=tk.NW,
                              pady=(1, 0))
