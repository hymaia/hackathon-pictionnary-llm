import tkinter as tk

from src.paint import PaintApp


def main():
    root = tk.Tk()
    root.title("Paint Application")
    _ = PaintApp(root)
    root.mainloop()
