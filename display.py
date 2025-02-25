import tkinter as tk
import matplotlib.pyplot as plt 
from generator import ObjectGenerator
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from design.model import figure


class Display3D: 
    
    def __init__(self, root):
        self.root = root
        self.root.title("Object Visualization")
        self.size = 10
        self.objects = []
        self.generator = ObjectGenerator()


        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.TOP, fill=tk.X)

        self.create_button1 = tk.Button(
            self.frame,
            text = 'Generate Shapes',
            command = self.generate_shapes
        )
        self.create_button1.pack(side=tk.LEFT, padx=5, pady=5)

        self.create_button2 = tk.Button(
            self.frame,
            text = 'Generate Models',
            command = self.generate_model
        )
        self.create_button2.pack(side=tk.RIGHT, padx=5, pady=5)

        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.anim = FuncAnimation(
            self.fig, self.update, frames=360, interval=20, blit=True
        )




    def generate_shapes(self): 
        self.objects = []
        count = 55
        for i in range(0, count): 
            self.objects.append(self.generator.generate_object())
        self.update_plot()


    def generate_model(self):
        self.objects = []
        self.model = figure()
        self.objects = self.model.build()

        self.update_plot(-10, 50)


    def update_plot(self, minVal=-100, maxVal=100):
        self.ax.clear()
        
        self.ax.set_xlim(minVal, maxVal)
        self.ax.set_ylim(minVal, maxVal)
        self.ax.set_zlim(minVal, maxVal)
        
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



if __name__ == '__main__':
    
    root = tk.Tk()
    test = Display3D(root)
    root.geometry('600x600')
    root.mainloop()