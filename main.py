import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class App(tk.Tk):

    def __init__(self, title: str, size: tuple):

        # window setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.rowconfigure(0, weight=1)

        # window widgets and their positions on grid
        self.menu = Menu(self)
        self.menu.grid(row=0, column=1)

        self.image_area = ImageArea(self)
        self.image_area.grid(column=1, columnspan=3, row=0, sticky="nsew")

        # run
        self.mainloop()


class Menu(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):
        pass


class ImageArea(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(background="black", bd=0, highlightthickness=0, relief="ridge")

        # to be changed --> button upload
        self.image_original = Image.open("lofico_study_beach.jpg")
        self.image_ratio = self.image_original.size[0] / self.image_original.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image_original)

        self.bind("<Configure>", self.show_full_image)

    def show_full_image(self, event):

        # current canvas ratio
        self.canvas_ratio = event.width / event.height

        if self.canvas_ratio > self.image_ratio:
            self.height = int(event.height)
            self.width = int(self.height * self.image_ratio)
        else:
            self.width = int(event.width)
            self.height = int(self.width / self.image_ratio)

        self.resized_image = self.image_original.resize((self.width, self.height))
        self.resized_tk = ImageTk.PhotoImage(self.resized_image)
        self.create_image(
            int(event.width / 2),
            int(event.height / 2),
            anchor="center",
            image=self.resized_tk,
        )


App(title="My App", size=(800, 600))
