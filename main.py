import tkinter as tk
from tkinter import ttk


class App(tk.Tk):

    def __init__(self, title: str, size: tuple):

        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # widgets
        self.menu = Menu(self)

        # run
        self.mainloop()


class Menu(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)

        self.create_widgets()

    def create_widgets(self):

        # create the widgets
        menu_button_1 = ttk.Button(self, text="Button 1")
        menu_button_2 = ttk.Button(self, text="Button 2")
        menu_button_3 = ttk.Button(self, text="Button 3")

        menu_slider_1 = ttk.Scale(self, orient="vertical")
        menu_slider_2 = ttk.Scale(self, orient="vertical")

        toggle_frame = ttk.Frame(self)
        menu_toggle_1 = ttk.Checkbutton(toggle_frame, text="check 1")
        menu_toggle_2 = ttk.Checkbutton(toggle_frame, text="check 2")

        entry = ttk.Entry(self)

        # create the grid
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # place the widgets
        menu_button_1.grid(row=0, column=0, sticky="nswe", columnspan=2)
        menu_button_2.grid(row=0, column=2, sticky="nswe")
        menu_button_3.grid(row=1, column=0, columnspan=3, sticky="nsew")

        menu_slider_1.grid(row=2, column=0, rowspan=2, sticky="nsew", pady=20)
        menu_slider_2.grid(row=2, column=2, rowspan=2, sticky="nsew", pady=20)

        # toggle layout
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
        menu_toggle_1.pack(side="left", expand=True)
        menu_toggle_2.pack(side="left", expand=True)

        # entry layout
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


App(title="My App", size=(600, 400))
