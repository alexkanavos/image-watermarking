import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class App(tk.Tk):

    def __init__(self, title: str, size: tuple):

        # window setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure(0, weight=1)

        # window widgets and their position on the window grid
        self.menu = Menu(self)
        self.menu.grid(row=0, column=0, sticky="nsew")

        self.image_area = ImageArea(self)
        self.image_area.grid(row=0, column=1, columnspan=2, sticky="nsew")

        # run
        self.mainloop()


class Menu(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.configure(padding=20)
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform="a")

        self.create_widgets()

    def create_widgets(self):

        # Open Image Button
        self.button_open = ttk.Button(self, text="Open Image")
        self.button_open.grid(row=0, column=0, columnspan=2, sticky="n")

        # Watermark
        self.watermark_label = ttk.Label(self, text="Watermark: ")
        self.watermark_label.grid(row=1, column=0, sticky="e")

        self.watermark_entry = ttk.Entry(self)
        self.watermark_entry.grid(row=1, column=1, sticky="w")

        # X-Position
        self.x_position_label = ttk.Label(self, text="X-Position: ")
        self.x_position_label.grid(row=2, column=0, sticky="e")

        self.x_position_entry = ttk.Entry(self)
        self.x_position_entry.grid(row=2, column=1, sticky="w")

        # Y-Position
        self.y_position_label = ttk.Label(self, text="Y-Position: ")
        self.y_position_label.grid(row=3, column=0, sticky="e")

        self.y_position_entry = ttk.Entry(self)
        self.y_position_entry.grid(row=3, column=1, sticky="w")

        # Angle
        self.angle_label = ttk.Label(self, text="Angle: ")
        self.angle_label.grid(row=4, column=0, sticky="e")

        self.angle_entry = ttk.Entry(self)
        self.angle_entry.grid(row=4, column=1, sticky="w")

        # Preview Image Button
        self.button_preview = ttk.Button(self, text="Preview")
        self.button_preview.grid(row=5, column=0, columnspan=2, sticky="s")

        # Save Image Button
        self.button_save = ttk.Button(self, text="Save Image")
        self.button_save.grid(row=6, column=0, columnspan=2, sticky="s")


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
