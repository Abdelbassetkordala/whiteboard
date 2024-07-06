import tkinter as tk
from tkinter import filedialog
from PIL import ImageGrab

class Whiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Whiteboard")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(root, bg='white', width=800, height=600)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.old_x = None
        self.old_y = None
        self.paint_color = 'black'

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X)

        self.create_buttons()

        self.color_palette = tk.Frame(root)
        self.color_palette.pack(fill=tk.X)
        self.create_color_buttons()

    def create_buttons(self):
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear, bg='red', fg='white')
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save, bg='blue', fg='white')
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.eraser_button = tk.Button(self.button_frame, text="Eraser", command=self.use_eraser, bg='grey', fg='white')
        self.eraser_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.brush_button = tk.Button(self.button_frame, text="Brush", command=self.use_brush, bg='black', fg='white')
        self.brush_button.pack(side=tk.LEFT, padx=5, pady=5)

    def create_color_buttons(self):
        colors = ['black', 'red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink']
        for color in colors:
            button = tk.Button(self.color_palette, bg=color, width=2, command=lambda col=color: self.set_color(col))
            button.pack(side=tk.LEFT, padx=5, pady=5)

    def set_color(self, color):
        self.paint_color = color

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                    width=5, fill=self.paint_color, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def clear(self):
        self.canvas.delete("all")

    def save(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("All files", "*.*")])
        if file_path:
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

    def use_eraser(self):
        self.paint_color = 'white'

    def use_brush(self):
        self.paint_color = 'black'

def main():
    root = tk.Tk()
    app = Whiteboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
