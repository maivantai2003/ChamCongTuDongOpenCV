from PIL import ImageTk, Image
import datetime
import tkinter as tk
from tkinter import StringVar, messagebox, Canvas, Frame, BOTH, NW

class Button(tk.Button):
    def __init__(self, master,image,title,width,height) -> None:
        super().__init__(master)
        if title != "":
            self.config(text=title)
        self.canvas = tk.Canvas(self,width=width,height = height)
        self.config(background="#1c2341")
        self.config(relief=tk.FLAT)
        img= (Image.open(image))
        resized_image= img.resize((width,height), Image.ANTIALIAS)
        self.new_image= ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.new_image)
        self.config(image = self.new_image)


        