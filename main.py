import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class App(tk.Tk):

    def __init__(self, title: str, size: tuple):

        # main setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(0, weight=1)

        # widgets
        self.menu = Menu(self)
        self.menu.grid(row=0, column=1)
        self.image_area = ImageArea(self)
        self.image_area.grid(row=0, column=0)

        # run
        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.75, y=40, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):

        self.text_label = ttk.Label(self, text="Watermark")
        self.text_entry = ttk.Entry(self)

        self.font_family_label = ttk.Label(self, text="Font Family")
        self.font_family_entry = ttk.Entry(self)

        self.font_size_label = ttk.Label(self, text="Font Size")
        self.font_size_entry = ttk.Entry(self)

        # create the grid
        self.columnconfigure((0), weight=1, uniform="col")
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform="row")

        # place the widgets
        self.text_label.grid(row=0, column=0, sticky="ws")
        self.text_entry.grid(row=1, column=0, sticky="wn")

        self.font_family_label.grid(row=2, column=0, sticky="ws")
        self.font_family_entry.grid(row=3, column=0, sticky="wn")

        self.font_size_label.grid(row=4, column=0, sticky="ws")
        self.font_size_entry.grid(row=5, column=0, sticky="wn")


class ImageArea(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent)

    # def import_image(self):
    #     self.image_original = Image.open("lofico_study_beach.jpg")
    #     self.image_ratio = self.image_original.size[0] / self.image_original.size[1]
    #     self.image_tk = ImageTk.PhotoImage(self.image_original)


App(title="My App", size=(800, 600))
