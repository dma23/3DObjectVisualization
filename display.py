import tkinter as tk
import matplotlib.pyplot as plt 
from generator import ObjectGenerator
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Display3D: 
    
    def __init__(self, root):
        self.root = root
        self.root.title("Display Shapes")
        self.size = 10
        self.objects = []
        self.generator = ObjectGenerator()

        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.anim = FuncAnimation(
            self.fig, self.update, interval=50, blit=50
        )

        self.generate_shapes()


    def generate_shapes(self): 
        count = 1 
        self.objects.append(self.generator.generate_object())
        self.update_plot()


    def update_plot(self):
        """Update the 3D plot with the current objects"""
        self.ax.clear()
        
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_zlim(-10, 10)
        
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title('3D Display')
        
        for i in range(0, len(self.objects)):
                collection = self.objects[i].get_collection()
                if collection:
                    self.ax.add_collection3d(collection)
        
        self.canvas.draw()
    

    def update(self, frame):
        self.ax.view_init(elev=30, azim=frame % 360)
        return self.ax,