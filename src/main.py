import tkinter as tk

from src.paint import PaintApp
from src.game import Game

def main():
    root = tk.Tk()
    root.title("Pictionnary vs LLM")

    game = Game()
    _ = PaintApp(root, game)
    root.mainloop()

if __name__ == "__main__":
    main()