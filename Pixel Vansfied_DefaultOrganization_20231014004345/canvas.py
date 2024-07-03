'''
This file contains the Canvas class which represents the drawing canvas in the Pixel Vansfied application.
'''
import tkinter as tk
import tkinter.filedialog as tkfiledialog
import tkinter.colorchooser as tkcolorchooser
class Canvas(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=800, height=600, bg="white")
        self.parent = parent
        self.current_color = "black"
        self.undo_stack = []
        self.redo_stack = []
        self.bind("<Button-1>", self.start_drawing)
        self.bind("<B1-Motion>", self.draw)
        self.bind("<ButtonRelease-1>", self.stop_drawing)
    def start_drawing(self, event):
        self.undo_stack.append(self.postscript(colormode="color"))
        self.redo_stack.clear()
        self.draw(event)
    def draw(self, event):
        x, y = event.x, event.y
        self.create_rectangle(x, y, x+1, y+1, fill=self.current_color, outline=self.current_color)
    def stop_drawing(self, event):
        self.undo_stack.append(self.postscript(colormode="color"))
    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.postscript(colormode="color"))
            self.delete("all")
            self.postscript(file="temp.ps", colormode="color")
            self.undo_stack.pop()
            self.load_file("temp.ps")
    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.postscript(colormode="color"))
            self.delete("all")
            self.postscript(file="temp.ps", colormode="color")
            self.load_file(self.redo_stack.pop())
    def new_file(self):
        self.delete("all")
        self.undo_stack.clear()
        self.redo_stack.clear()
    def save_file(self):
        filename = tkfiledialog.asksaveasfilename(defaultextension=".ps", filetypes=[("PostScript files", "*.ps")])
        if filename:
            self.postscript(file=filename, colormode="color")
    def load_file(self, filename):
        self.delete("all")
        self.postscript(file=filename, colormode="color")
    def choose_color(self):
        color = tkcolorchooser.askcolor(title="Choose Color")
        if color:
            self.current_color = color[1]