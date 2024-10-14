import os
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkf
import tkinter.filedialog as tkfd

from src import assets, _ROOT
from src.app import utils


class FileEntry(ttk.Frame):
    def __init__(self,
                 parent: tk.Misc,
                 font: tkf.Font | tuple | None=None,
                 entry_style: str | None=None,
                 button_style: str='FileEntry.TButton',
                 file_types: tuple[str, str] | list[tuple[str, str]] = ('All Files', '*.*'),
                 dialog_text: str='Select a File',
                 initial_dir: str | None=None,
                 initial_file: str | None=None,
                 **kwargs):
        super().__init__(parent)

        self._file_types = file_types
        self._fd_text = dialog_text
        self._entry_style = entry_style or 'TEntry'
        self._btn_style = button_style
        self._init_dir = initial_dir or os.path.normpath(os.path.join(_ROOT, '..'))
        self._init_file = initial_file

        padding = utils.get_style(self._btn_style, 'padding', None)
        if isinstance(padding, str):
            if ' ' in padding:
                _, pady_str = padding.split(' ')
            else:
                pady_str = padding
            pady = int(pady_str)
        elif padding is None:
            pady = 0
        else:
            pady = padding

        self._entry_var = tk.StringVar(self)
        self._entry = ttk.Entry(self,
                                font=font,
                                style=self._entry_style,
                                textvariable=self._entry_var,
                                **kwargs)
        self._entry.pack(side=tk.LEFT,
                         anchor=tk.W,
                         fill=tk.X,
                         expand=tk.TRUE,
                         ipady=int(pady) * 4)

        self._entry.update()
        height = self._entry.winfo_reqheight()
        self._folder_img = assets.get_tkimage('folder.png',
                                              size=height - 8,
                                              relative='height')
        self._btn = ttk.Button(self,
                               style=self._btn_style,
                               image=self._folder_img,
                               padding=0,
                               cursor='hand2',
                               command=self._on_click)
        self._btn.pack(side=tk.LEFT,
                       anchor=tk.E)

    def _on_click(self, event: tk.Event | None=None) -> None:
        file_types: list[tuple[str, str]]
        if isinstance(self._file_types, tuple):
            file_types = [self._file_types]
        else:
            file_types = self._file_types

        init_file = self._init_file
        cur_selection = self._entry_var.get()
        if init_file is None and cur_selection != '':
            init_file = cur_selection

        tkfd.askopenfilename(title=self._fd_text,
                             filetypes=file_types,
                             typevariable=self._entry_var,
                             initialdir=self._init_dir,
                             initialfile=init_file)

    def get(self) -> str:
        return self._entry_var.get()
