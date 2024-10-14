import tkinter as tk
import tkinter.ttk as ttk

from src.app.widgets import Frame, Page, ScrollableFrame


class ProgressView(Page):
    def __init__(self, parent: tk.Misc, style='Page.TFrame', **kw):
        super().__init__(parent, style=style, **kw)

        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure((1), weight=0)
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_columnconfigure((1), weight=0)

        container = Frame(self, style=self.style)
        container.grid(row=1,
                       column=1,
                       sticky=tk.NSEW)

        self.console = ScrollableFrame(container)
        self.console.pack(side=tk.TOP,
                          anchor=tk.NW,
                          fill=tk.BOTH,
                          expand=tk.TRUE)

        self.prog_var = tk.IntVar(container, 0)
        self.prog_bar = ttk.Progressbar(container,
                                        variable=self.prog_var)
        self.prog_bar.pack(side=tk.TOP,
                           anchor=tk.NW,
                           fill=tk.X,
                           after=self.console)

        btn_container = Frame(container, style=container.style)
        btn_container.pack(side=tk.TOP,
                           anchor=tk.NW,
                           fill=tk.X,
                           after=self.prog_bar)

        self.next_btn = ttk.Button(btn_container, text='View Results')
        self.next_btn.pack(side=tk.RIGHT,
                           anchor=tk.E)

        self.back_btn = ttk.Button(btn_container, text='Back')
        self.back_btn.pack(side=tk.LEFT,
                           anchor=tk.W)

    @property
    def key(self) -> str:
        return 'progress'

    def show(self):
        self.console.clear()
        self.prog_var.set(0)
        self.tkraise()
