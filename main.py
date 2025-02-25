import tkinter as tk
from display import Display3D

def main():
    root = tk.Tk()
    app = Display3D(root)
    root.geometry("800x800")
    root.mainloop()

if __name__ == "__main__":
    main()