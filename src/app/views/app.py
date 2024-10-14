import math
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkf
from typing import Literal, Callable

from src import assets
from src.app.exceptions import GUIError


class App(ttk.Frame):
    def __init__(self, parent: ttk.Frame, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid(row=0, column=0, sticky=tk.NSEW)

        parent.update()
        window_width = parent.winfo_width()
        window_height = parent.winfo_height()

        navbar_width = math.ceil(window_width * (1 / 7))
        footer_height = math.ceil(window_height * (1 / 11))

        self.grid_columnconfigure((0), weight=0)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0), weight=1)
        self.grid_rowconfigure((1), weight=0)

        self.navbar = navbar = NavBar(self, width=navbar_width)
        navbar.grid(row=0,
                    rowspan=2,
                    column=0,
                    sticky=tk.NSEW)

        self.footer = footer = Footer(self, height=footer_height)
        footer.grid(row=1,
                    column=1,
                    sticky=tk.NSEW)

        self.container = ttk.Frame(self)
        self.container.grid(row=0,
                            column=1,
                            sticky=tk.NSEW)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.post_process()

    def set_nav(self,
                nav: Literal['home', 'parser', 'summarizer', 'perm_qa_qc']
               ) -> None:
        self.navbar.navbar_list.set_active(nav)

    def post_process(self) -> None:
        self.navbar.post_process()
        self.footer.post_process()


class NavBar(ttk.Frame):
    def __init__(self, parent: App, **kwargs):
        super().__init__(parent, style='NavBar.TFrame', **kwargs)

        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0), weight=2)
        self.grid_rowconfigure((1), weight=6)
        self.grid_rowconfigure((1), weight=8)
        self.grid_propagate(False)

        self.navbar_list = NavBarList(self)
        self.navbar_list.grid(row=1,
                              column=0,
                              sticky=tk.NSEW)

    def post_process(self) -> None:
        self.update()
        self.navbar_list.post_process()


class NavBarList(ttk.Frame):
    def __init__(self, parent: NavBar, **kwargs):
        super().__init__(parent, style='List.NavBar.TFrame', **kwargs)

        self.dashboard_item = NavBarListItem(self,
                                             text='HOME',
                                             icon='home.png')
        self.dashboard_item.pack(side=tk.TOP,
                                 anchor=tk.NW)

        self.parser_item = NavBarListItem(self,
                                          text='PARSER',
                                          icon='brackets.png')
        self.parser_item.pack(side=tk.TOP,
                              anchor=tk.NW)

        self.summarizer_item = NavBarListItem(self,
                                              text='SUMMARIZER',
                                              icon='pdf.png')
        self.summarizer_item.pack(side=tk.TOP,
                                  anchor=tk.NW)

        self.perm_qa_qc_item = NavBarListItem(self,
                                              text='PERMUTATIONS QA/QC',
                                              icon='valid-document.png')
        self.perm_qa_qc_item.pack(side=tk.TOP,
                                  anchor=tk.NW)

        self.dashboard_item._set_state('active')

    @property
    def _items(self) -> list['NavBarListItem']:
        return list(
            filter(
                lambda child: isinstance(child, NavBarListItem),
                self.winfo_children()
            )
        )

    def clear_activity(self) -> None:
        for item in self._items:
            item._set_state('normal')

    def set_active(self,
                   nav: Literal['home', 'parser', 'summarizer', 'perm_qa_qc']
                  ) -> None:
        nav_widget: NavBarListItem | None = None
        match nav:
            case 'home':
                nav_widget = self.dashboard_item
            case 'parser':
                nav_widget = self.parser_item
            case 'summarizer':
                nav_widget = self.summarizer_item
            case 'perm_qa_qc':
                nav_widget = self.perm_qa_qc_item
            case other:
                raise GUIError(f'Unknown navigation option: {other}')

        self.clear_activity()
        nav_widget._set_state('active')

    def post_process(self) -> None:
        self.update()
        for item in self._items:
            item.post_process()


class NavBarListItem(ttk.Frame):
    def __init__(self,
                 parent: NavBarList,
                 text: str,
                 icon: str,
                 height: int=40,
                 width: int | None=None,
                 cursor: str='hand2',
                 style: str='Item.List.NavBar.TFrame',
                 event: Callable[[tk.Event | None], None] | None=None,
                 **kwargs):
        super().__init__(parent, cursor=cursor, style=style, **kwargs)

        self.parent = parent
        self._icon = icon
        self._height = height
        self._width = width
        self._state: Literal['hover', 'active', 'normal'] = 'normal'
        self._event = event

        self.accent_frame = ttk.Frame(self, style='Item.List.NavBar.TFrame')
        self.img_label = ttk.Label(self, style='List.NavBar.TLabel')
        self.label = ttk.Label(self, text=text, style='List.NavBar.TLabel')

        self.bind('<Button-1>', self._on_click)
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)

        for child in self.winfo_children():
            child.bind('<Button-1>', self._on_click)

        self._set_state('normal')

    def _on_click(self, event: tk.Event | None=None) -> None:
        """Styles the list item to the `active` state and calls the
        configured event if one exists.
        """

        if self._state == 'active':
            return

        self.parent.clear_activity()
        self._set_state('active')
        if self._event is not None:
            try:
                self._event(event)
            except TypeError:
                self._event()

    def _on_enter(self, event: tk.Event | None=None) -> None:
        """Styles the list item to the `hover` state."""

        if self._state == 'hover' or self._state == 'active':
            return

        self._set_state('hover')

    def _on_leave(self, event: tk.Event | None=None) -> None:
        """Styles the list item to the `normal` state."""

        if self._state == 'normal' or self._state == 'active':
            return

        self._set_state('normal')

    def _set_state(self, state: Literal['hover', 'active', 'normal']) -> None:
        match state:
            case 'hover':
                self.configure(cursor='hand2')
                self.configure(style='Highlight.Item.List.NavBar.TFrame')
                self.img_label.configure(style='Highlight.List.NavBar.TLabel')
                self.label.configure(style='Highlight.List.NavBar.TLabel')
                self.accent_frame.configure(style='Highlight.Item.List.NavBar.TFrame')
            case 'active':
                self.configure(cursor='arrow')
                self.configure(style='Highlight.Item.List.NavBar.TFrame')
                self.img_label.configure(style='Highlight.List.NavBar.TLabel')
                self.label.configure(style='Highlight.List.NavBar.TLabel')
                self.accent_frame.configure(style='Accent.Item.List.NavBar.TFrame')
            case 'normal':
                self.configure(cursor='hand2')
                self.configure(style='Item.List.NavBar.TFrame')
                self.img_label.configure(style='List.NavBar.TLabel')
                self.label.configure(style='List.NavBar.TLabel')
                self.accent_frame.configure(style='Item.List.NavBar.TFrame')
            case other:
                raise RuntimeError(f'Unknown state: {other}')

        self._state = state

    def post_process(self) -> None:
        parent_width = self.parent.winfo_width()
        self.configure(width=self._width or parent_width * 1.5,
                       height=self._height)

        self.update()
        height = self.winfo_height()
        width = self.winfo_width()
        
        accent_width = width / 40
        self.accent_frame.place(x=0,
                                y=0,
                                height=height,
                                width=accent_width)

        img_padx = 5
        label_height = tkf.Font(font=self.label['font']).metrics('linespace')
        img_height = math.floor(label_height + 1)
        self._icon_img = assets.get_tkimage(self._icon,
                                            img_height,
                                            'height',
                                            parent=self)

        label_x = accent_width + img_padx * 3 + self._icon_img.width() + 5
        self.label.place(x=label_x,
                         y=height / 2 - label_height / 2,
                         width=width - label_x)

        self.img_label.configure(image=self._icon_img)
        self.img_label.place(x=accent_width + img_padx * 2,
                             height=img_height + 2,
                             width=self._icon_img.width() + 2,
                             y=height / 2 - img_height / 2 - 1)

    def set_event(self, event: Callable[[tk.Event | None], None]) -> None:
        self._event = event


class Footer(ttk.Frame):
    def __init__(self, parent: App, **kwargs):
        super().__init__(parent, style='Footer.TFrame', **kwargs)

        self.grid_rowconfigure((0), weight=1)
        self.grid_columnconfigure((0), weight=12)
        self.grid_columnconfigure((1), weight=1)
        self.grid_propagate(False)

        self.img_label = tk.Label(self, bg='#6b6b6b', borderwidth=0)
        self.img_label.grid(row=0,
                            column=1,
                            sticky=tk.NSEW)

    def post_process(self) -> None:
        self.update()
        frame_height = self.winfo_height()
        img_height = math.floor(frame_height * 0.5)
        self._etrm_img = assets.get_tkimage('etrm-logo-gray.png',
                                            img_height,
                                            'height',
                                            parent=self)
        self.img_label.configure(image=self._etrm_img)
        self.configure(height=78)
