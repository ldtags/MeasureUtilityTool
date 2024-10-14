import tkinter as tk
import tkinter.ttk as ttk

def set_frame_styles(style: ttk.Style) -> None:
    style.configure(
        'Frame',
        background='#dfe2e7'
    )

    style.configure(
        'TFrame',
        background='#dfe2e7'
    )

    style.configure(
        'Testing.TFrame',
        background='green'
    )

    style.configure(
        'NavBar.TFrame',
        background='#6b6b6b',
        width=300
    )

    style.configure(
        'List.NavBar.TFrame'
    )

    style.configure(
        'Item.List.NavBar.TFrame',
        cursor='hand2'
    )

    style.configure(
        'Accent.Item.List.NavBar.TFrame',
        background='#6e9460'
    )

    style.configure(
        'Highlight.Item.List.NavBar.TFrame',
        background='#4e4e4e'
    )

    style.configure(
        'Highlight.Item.List.NavBar.TFrame',
        background='#4e4e4e'
    )

    style.configure(
        'Active.Item.List.NavBar.TFrame',
        background='#5c5c5c'
    )

    style.configure(
        'Footer.TFrame',
        background='#6b6b6b'
    )

    style.configure(
        'Dashboard.TFrame'
    )

    style.configure(
        'Form.TFrame',
        background='#ffffff',
        borderwidth=1,
        bordercolor='#bfbfbf'
    )

    style.configure(
        'Page.TFrame',
        background='#dfe2e7'
    )


def set_label_styles(style: ttk.Style) -> None:
    style.configure(
        'TLabel',
        font=('Segoe UI', 12)
    )

    style.configure(
        'NavBar.TLabel',
        background='#6b6b6b',
        foreground='#ffffff'
    )
    style.configure(
        'List.NavBar.TLabel',
        foreground='#ffffff',
        font=('Bahnschrift Light', 10, 'bold')
    )

    style.configure(
        'Highlight.List.NavBar.TLabel',
        background='#4e4e4e'
    )

    style.configure(
        'Active.List.NavBar.TLabel',
        background='#5c5c5c'
    )

    style.configure(
        'Icon.List.NavBar.TLabel'
    )

    style.configure(
        'Header.Section.TLabel',
        background='#dfe2e7',
        font=('Segoe UI', 10, 'bold')
    )

    style.configure(
        'Form.TLabel',
        background='#ffffff'
    )

    style.configure(
        'Item.Form.TLabel',
        font=('Segoe UI', 9)
    )

    style.configure(
        'Header.Form.TLabel',
        font=('Segoe UI', 10, 'bold')
    )

    style.configure(
        'Title.View.TLabel',
        font=('Segoe UI', 12, 'bold'),
        background='#dfe2e7'
    )


def set_button_styles(style: ttk.Style) -> None:
    style.configure(
        'TButton',
        font=('Segoe UI', 9),
        cursor='hand2',
        background='#bfbfbf',
        foreground='#000000',
        activebackground='#8c8c8c',
        highlightbackground='#9d9d9d',
        bordercolor='#898989'
    )

    style.configure(
        'Dashboard.Option.TButton',
        compound=tk.TOP
    )

    style.configure(
        'FileEntry.TButton',
        padding=0,
        borderwidth=1,
        font=('Segoe UI', 9)
    )

    style.configure(
        'Form.TButton',
        font=('Segoe UI', 9)
    )


def set_entry_styles(style: ttk.Style) -> None:
    style.configure(
        'Form.TEntry',
        background='#ffffff',
        borderwidth=1,
        relief=tk.FLAT,
        font=('Segoe UI', 9)
    )


def set_sep_styles(style: ttk.Style) -> None:
    style.configure(
        'Title.View.TSeparator',
        background='#000000'
    )

    style.configure(
        'Form.TSeparator',
        background='#ffffff'
    )


def set_cb_styles(style: ttk.Style) -> None:
    style.configure(
        'Form.TCheckbutton',
        background='#ffffff',
        font=('Segoe UI', 8)
    )


def set_styles() -> None:
    style = ttk.Style()
    set_frame_styles(style)
    set_label_styles(style)
    set_button_styles(style)
    set_entry_styles(style)
    set_sep_styles(style)
    set_cb_styles(style)
