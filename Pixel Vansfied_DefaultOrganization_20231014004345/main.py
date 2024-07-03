'''
This is the main file of the Pixel Vansfied application. It initializes the GUI and handles user interactions.
'''
import tkinter as tk
from canvas import Canvas
class PixelVansfiedApp:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root)
        self.canvas.pack()
        self.create_menu()
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.canvas.new_file)
        file_menu.add_command(label="Save", command=self.canvas.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.canvas.undo)
        edit_menu.add_command(label="Redo", command=self.canvas.redo)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        color_menu = tk.Menu(menu_bar, tearoff=0)
        color_menu.add_command(label="Choose Color", command=self.canvas.choose_color)
        menu_bar.add_cascade(label="Color", menu=color_menu)
        self.root.config(menu=menu_bar)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pixel Vansfied")
    app = PixelVansfiedApp(root)
    root.mainloop()