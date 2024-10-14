import tkinter as tk
import tkinter.ttk as ttk
import customtkinter as ctk

from src.app import utils
from src.app.widgets import Page, Frame, Separator, FileEntry


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

        container_style = 'Form.TFrame'
        bg = utils.get_style(container_style, 'background', 'transparent')
        bd = utils.get_style(container_style, 'borderwidth', 0)
        bc = utils.get_style(container_style, 'bordercolor', 'transparent')
        container = ctk.CTkFrame(self,
                                 fg_color=bg,
                                 border_width=bd,
                                 border_color=bc,
                                 corner_radius=8)
        container.grid(row=2,
                       column=1,
                       sticky=tk.NSEW)

        container.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=0)
        container.grid_columnconfigure((0), weight=1)

        self.json_switch_var = tk.IntVar(container, 1)
        self.json_switch = ctk.CTkSwitch(container,
                                         text='From this PC',
                                         text_color='#000000',
                                         button_color='#bfbfbf',
                                         button_hover_color='#9d9d9d',
                                         bg_color=bg,
                                         variable=self.json_switch_var)
        self.json_switch.grid(row=0,
                              column=0,
                              sticky=tk.NW,
                              padx=(20, 20),
                              pady=(10, 0))

        self.json_frame = JsonFrame(container)
        self.json_frame.grid(row=1,
                             column=0,
                             sticky=tk.NSEW,
                             padx=(30, 30))

        separator = Separator(container, color='#bfbfbf')
        separator.grid(row=2,
                       column=0,
                       sticky=tk.EW,
                       pady=(20, 10))

        self.etrm_switch_var = tk.IntVar(container, 0)
        self.etrm_switch = ctk.CTkSwitch(container,
                                         text='From the eTRM',
                                         text_color='#000000',
                                         button_color='#bfbfbf',
                                         button_hover_color='#9d9d9d',
                                         bg_color=bg,
                                         variable=self.etrm_switch_var)
        self.etrm_switch.grid(row=3,
                              column=0,
                              sticky=tk.NW,
                              padx=(20, 20))

        self.etrm_frame = EtrmFrame(container)
        self.etrm_frame.grid(row=4,
                             column=0,
                             sticky=tk.NSEW,
                             padx=(30, 30),
                             pady=(0, 20))

        self.parse_btn = ttk.Button(self,
                                    text='Parse Measure',
                                    style='Form.TButton',
                                    cursor='hand2')
        self.parse_btn.grid(row=3,
                            column=1,
                            sticky=tk.N,
                            pady=(10, 0),
                            ipadx=8)

    @property
    def key(self) -> str:
        return 'parser'

    def show(self) -> None:
        self.tkraise()

class JsonFrame(Frame):
    def __init__(self, parent: ParserView, **kw):
        super().__init__(parent, style='Form.TFrame', **kw)

        self.label = ttk.Label(self,
                               text='Select an eTRM Measure JSON File',
                               style='Item.Form.TLabel')
        self.label.pack(side=tk.TOP,
                        anchor=tk.NW,
                        fill=tk.X,
                        padx=(10, 10),
                        pady=(10, 0))

        self.file_entry = FileEntry(self, file_types=('JSON File', '*.json'))
        self.file_entry.pack(side=tk.TOP,
                             anchor=tk.NW,
                             fill=tk.X,
                             padx=(10, 10),
                             pady=(2, 0))


class EtrmFrame(Frame):
    def __init__(self, parent: ParserView, **kw):
        super().__init__(parent, style='Form.TFrame', **kw)

        etrm_label = ttk.Label(self,
                               text='Enter an eTRM Measure Version ID',
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
