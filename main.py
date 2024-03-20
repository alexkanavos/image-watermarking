import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class App(ttk.Window):

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
        self.place(x=0, y=0, relwidth=1, height=40)

        self.create_widgets()

    def create_widgets(self):

        # create the widgets
        self.menu_button_1 = ttk.Button(
            self, text="Close App", bootstyle=(DANGER, OUTLINE)
        )
        self.menu_button_2 = ttk.Button(
            self, text="Add Image", bootstyle=(PRIMARY, OUTLINE)
        )
        self.menu_button_3 = ttk.Button(
            self, text="Next Step", bootstyle=(INFO, OUTLINE)
        )

        # create the grid

        self.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="col")
        self.rowconfigure((0), weight=1, uniform="row")

        # place the widgets
        self.menu_button_1.grid(row=0, column=0, padx=7, sticky="w")
        self.menu_button_2.grid(row=0, column=2)
        self.menu_button_3.grid(row=0, column=4, padx=7, sticky="e")


App(title="My App", size=(600, 400))
