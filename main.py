import tkinter as tk
from display import Display3D
from design.model import figure

def main():
    root = tk.Tk()
    app = Display3D(root)
    root.geometry("1200x1200")
    root.mainloop()

if __name__ == "__main__":
    main()