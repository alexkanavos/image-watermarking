import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import os

os.environ["DISPLAY"] = ":0"


class App(tk.Tk):

    def __init__(self, title: str, size: tuple):

        # window setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
        self.rowconfigure(0, weight=1)

        # window widgets and their position on the window grid
        self.menu = Menu(self)
        self.menu.grid(row=0, column=0, sticky="nsew")

        self.image_area = ImageArea(self)
        self.image_area.grid(row=0, column=1, columnspan=3, sticky="nsew")

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
        self.button_open = ttk.Button(
            self, text="Open Image", command=self.upload_image
        )
        self.button_open.grid(row=0, column=0, columnspan=2, sticky="s")

        # Watermark
        self.watermark_label = ttk.Label(self, text="Watermark: ")
        self.watermark_label.grid(row=1, column=0, sticky="w")

        self.watermark_entry = ttk.Entry(self)
        self.watermark_entry.focus()
        self.watermark_entry.grid(row=1, column=1, sticky="we")
        self.watermark_entry.bind("<KeyRelease>", self.update_canvas_text)

        # Size
        self.size_label = ttk.Label(self, text="Size: ")
        self.size_label.grid(row=2, column=0, sticky="w")

        self.size_entry = ttk.Entry(self)
        self.size_entry.insert(tk.END, "12")
        self.size_entry.grid(row=2, column=1, sticky="we")
        self.size_entry.bind("<KeyRelease>", self.update_canvas_text)

        # Angle
        self.angle_label = ttk.Label(self, text="Angle: ")
        self.angle_label.grid(row=3, column=0, sticky="w")

        self.angle_entry = ttk.Entry(self)
        self.angle_entry.insert(tk.END, "0")
        self.angle_entry.grid(row=3, column=1, sticky="we")
        self.angle_entry.bind("<KeyRelease>", self.update_canvas_text)

        # X-Position
        self.x_position_label = ttk.Label(self, text="X-Position: ")
        self.x_position_label.grid(row=4, column=0, sticky="w")

        self.x_position_entry = ttk.Entry(self)
        self.x_position_entry.insert(tk.END, "400")
        self.x_position_entry.grid(row=4, column=1, sticky="we")
        self.x_position_entry.bind("<KeyRelease>", self.update_canvas_text)

        # Y-Position
        self.y_position_label = ttk.Label(self, text="Y-Position: ")
        self.y_position_label.grid(row=5, column=0, sticky="w")

        self.y_position_entry = ttk.Entry(self)
        self.y_position_entry.insert(tk.END, "300")
        self.y_position_entry.grid(row=5, column=1, sticky="we")
        self.y_position_entry.bind("<KeyRelease>", self.update_canvas_text)

        # Save Image Button
        self.button_save = ttk.Button(self, text="Save Image")
        self.button_save.grid(row=6, column=0, columnspan=2, sticky="n")

    def update_canvas_text(self, event):
        current_entries = {
            "watermark": str(self.watermark_entry.get()),
            "size": int(self.size_entry.get()),
            "angle": int(self.angle_entry.get()),
            "x_position": int(self.x_position_entry.get()),
            "y_position": int(self.y_position_entry.get()),
        }
        self.master.image_area.place_text(current_entries)

    def upload_image(self):
        self.master.image_area.open_image()


class ImageArea(tk.Canvas):

    def __init__(self, parent):
        super().__init__(parent)
        self.configure(background="black", bd=0, highlightthickness=0, relief="ridge")

        self.bind("<Configure>", self.show_full_image)

    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif")]
        )
        if file_path:
            self.image_original = Image.open(file_path)
            self.image_ratio = self.image_original.size[0] / self.image_original.size[1]
            self.image_tk = ImageTk.PhotoImage(self.image_original)
            self.show_full_image()

    def place_text(self, entries):
        self.delete("text")
        self.create_text(
            entries["x_position"],
            entries["y_position"],
            text=entries["watermark"],
            angle=entries["angle"],
            font=("Arial", entries["size"], "bold"),
            tags="text",
            fill="white",
        )

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
