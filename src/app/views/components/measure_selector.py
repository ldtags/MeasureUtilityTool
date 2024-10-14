import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk
from typing import Literal

from src.app import utils
from src.app.widgets import Frame, FileEntry, Separator


class MeasureSelectionFrame(ctk.CTkFrame):
    def __init__(self,
                 parent: tk.Misc,
                 file_text: str,
                 etrm_text: str,
                 file_types: tuple[str, str] | list[tuple[str, str]] = ('JSON Files', '*.json'),
                 dialog_text: str='Select a File',
                 style: str='Form.TFrame',
                 btn_text: str='Select Measure',
                 **kwargs):
        bg = utils.get_style(style, 'background', 'transparent')
        bd = utils.get_style(style, 'borderwidth', 0)
        bc = utils.get_style(style, 'bordercolor', 'transparent')
        super().__init__(parent,
                         fg_color=bg,
                         border_width=bd,
                         border_color=bc,
                         corner_radius=8,
                         **kwargs)

        self.state: Literal['json', 'etrm'] = 'json'

        self.grid_rowconfigure((0, 2, 4, 6, 7), weight=0)
        self.grid_rowconfigure((1, 3, 5, 8), weight=1)
        self.grid_columnconfigure((0), weight=1)

        self.json_switch_var = tk.IntVar(self, 1)
        self.json_switch = ctk.CTkSwitch(self,
                                         text='From this PC',
                                         text_color='#000000',
                                         button_color='#bfbfbf',
                                         button_hover_color='#9d9d9d',
                                         bg_color=bg,
                                         variable=self.json_switch_var,
                                         command=self.swap_state)
        self.json_switch.grid(row=0,
                              column=0,
                              sticky=tk.NSEW,
                              padx=(20, 20),
                              pady=(10, 0))

        self.json_frame = JsonFrame(self,
                                    text=file_text,
                                    file_types=file_types,
                                    dialog_text=dialog_text,
                                    button_text=btn_text)
        self.json_frame.grid(row=2,
                             column=0,
                             sticky=tk.NSEW,
                             padx=(30, 30))

        separator = Separator(self, color='#bfbfbf')
        separator.grid(row=4,
                       column=0,
                       sticky=tk.EW,
                       pady=(20, 10))

        self.etrm_switch_var = tk.IntVar(self, 0)
        self.etrm_switch = ctk.CTkSwitch(self,
                                         text='From the eTRM',
                                         text_color='#000000',
                                         button_color='#bfbfbf',
                                         button_hover_color='#9d9d9d',
                                         bg_color=bg,
                                         variable=self.etrm_switch_var,
                                         command=self.swap_state)
        self.etrm_switch.grid(row=6,
                              column=0,
                              sticky=tk.NSEW,
                              padx=(20, 20),
                              pady=(0, 10))

        self.etrm_frame = EtrmFrame(self,
                                    text=etrm_text,
                                    button_text=btn_text)
        self.etrm_frame.grid(row=7,
                             column=0,
                             sticky=tk.NSEW,
                             padx=(30, 30),
                             pady=(0, 20))

        self.set_state('json')
        self.grid_propagate(False)

    def swap_state(self, event: tk.Event | None=None) -> None:
        match self.state:
            case 'json':
                self.set_state('etrm')
            case 'etrm':
                self.set_state('json')
            case other:
                raise tk.TclError(f'Unknown state: {other}')

    def set_state(self, state: Literal['json', 'etrm']) -> None:
        match state:
            case 'json':
                self.etrm_frame.grid_forget()
                self.grid_rowconfigure((1, 3), weight=1)
                self.grid_rowconfigure((5, 8), weight=0)
                self.json_frame.grid(row=2,
                                     column=0,
                                     sticky=tk.NSEW,
                                     padx=(30, 30))
                self.json_switch_var.set(1)
                self.etrm_switch_var.set(0)
            case 'etrm':
                self.json_frame.grid_forget()
                self.grid_rowconfigure((1, 3), weight=0)
                self.grid_rowconfigure((5, 8), weight=1)
                self.etrm_frame.grid(row=7,
                                     column=0,
                                     sticky=tk.NSEW,
                                     padx=(30, 30),
                                     pady=(0, 20))
                self.json_switch_var.set(0)
                self.etrm_switch_var.set(1)
            case other:
                raise tk.TclError(f'Unknown state: {other}')

        self.state = state


class JsonFrame(Frame):
    def __init__(self,
                 parent: Frame,
                 text: str,
                 file_types: tuple[str, str] | list[tuple[str, str]],
                 dialog_text: str,
                 button_text: str,
                 **kw):
        super().__init__(parent, style='Form.TFrame', **kw)

        self.label = ttk.Label(self,
                               text=text,
                               style='Item.Form.TLabel')
        self.label.pack(side=tk.TOP,
                        anchor=tk.NW,
                        fill=tk.X,
                        padx=(10, 10),
                        pady=(10, 0))

        self.file_entry = FileEntry(self,
                                    file_types=file_types,
                                    dialog_text=dialog_text)
        self.file_entry.pack(side=tk.TOP,
                             anchor=tk.NW,
                             fill=tk.X,
                             padx=(10, 10),
                             pady=(2, 0))

        self.btn = ttk.Button(self, text=button_text)
        self.btn.pack(side=tk.BOTTOM,
                      anchor=tk.SE,
                      padx=(10, 10),
                      pady=(15, 0),
                      ipadx=8)


class EtrmFrame(Frame):
    def __init__(self,
                 parent: Frame,
                 text: str,
                 button_text: str,
                 **kw):
        super().__init__(parent, style='Form.TFrame', **kw)

        etrm_label = ttk.Label(self,
                               text=text,
                               style='Item.Form.TLabel')
        etrm_label.pack(side=tk.TOP,
                        anchor=tk.NW,
                        fill=tk.X,
                        padx=(10, 10),
                        pady=(10, 0))

        self.etrm_entry = ttk.Entry(self,
                                    style='Form.TEntry')
        self.etrm_entry.pack(side=tk.TOP,
                             anchor=tk.NW,
                             after=etrm_label,
                             fill=tk.X,
                             padx=(10, 10),
                             pady=(2, 0))

        key_label = ttk.Label(self,
                              text='Enter your eTRM API Key',
                              style='Item.Form.TLabel')
        key_label.pack(side=tk.TOP,
                       anchor=tk.NW,
                       after=self.etrm_entry,
                       fill=tk.X,
                       padx=(10, 10),
                       pady=(8, 0))

        self.key_entry = ttk.Entry(self,
                                   style='Form.TEntry')
        self.key_entry.pack(side=tk.TOP,
                            anchor=tk.NW,
                            after=key_label,
                            fill=tk.X,
                            padx=(10, 10),
                            pady=(2, 0))

        self.rm_var = tk.IntVar(self, 0)
        self.rm_checkbox = ttk.Checkbutton(self,
                                           text='Remember Me',
                                           variable=self.rm_var,
                                           style='Form.TCheckbutton',
                                           cursor='hand2')
        self.rm_checkbox.pack(side=tk.TOP,
                              anchor=tk.NW,
                              after=self.key_entry,
                              padx=(10, 10),
                              pady=(1, 0))

        self.btn = ttk.Button(self, text=button_text)
        self.btn.pack(side=tk.BOTTOM,
                      anchor=tk.SE,
                      padx=(10, 10),
                      pady=(0, 0),
                      ipadx=8)
