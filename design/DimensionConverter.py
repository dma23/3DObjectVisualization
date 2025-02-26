from tkinter import filedialog
import cv2
import numpy as np
from objects.shapes import Cube
from objects.shapes import Triangles
class imageConverter:

    def __init__(self):
        
        self.image = None
        self.mesh = []
        self.edge_detection = False
        self.depth_factor = 10
        self.resolution = 20

        self.load_image()
    

    def load_image(self):

        file_path = filedialog.askopenfilename(
            title='Select an image',
            filetypes=[('Image files', '*.jpg *.png *.jpeg')]
        )

        if file_path: 
            self.image = cv2.imread(file_path)
            if self.image is not None:
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                return True
            else:
                self.image_label.config(text='failed to load image')
                return False
    

    def detect_edges(self, img):

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) if len(img.shape) > 2 else img
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)

        return cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB) if len(img.shape) > 2 else edges
    

    def convert_to_3d(self):

        if self.image is None: 
            if not self.load_image():
                print('Image not loaded')
                return []
        

        self.objects = []
        
        h, w = self.image.shape[:2]

        max_dim = max(h, w)
        cell_size = max_dim / self.resolution

        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY) if len(self.image.shape) > 2 else self.image

        edges_gray = None
        if self.edge_detection:
            edges = self.detect_edges(self.image)
            edges_gray = cv2.cvtColor(edges, cv2.COLOR_RGB2GRAY) if len(edges.shape) > 2 else edges

        for y in range(0, h, max(1, int(cell_size))):

            for x in range(0, w, max(1, int(cell_size))):
                
                y_end = min(y + int(cell_size), h)
                x_end = min(x + int(cell_size), w)
                
                cell = self.image[y:y_end, x:x_end]

                if cell.size > 0:  # Ensure the cell is not empty
                    avg_color = np.mean(cell, axis=(0, 1))
                    color_hex = '#{:02x}{:02x}{:02x}'.format(int(avg_color[0]), int(avg_color[1]), int(avg_color[2]))

                    cell_gray = gray[y:y_end, x:x_end]
                    avg_brightness = np.mean(cell_gray)

                    depth = (255 - avg_brightness) / 255 * self.depth_factor

                    norm_x = (x / w - 0.5) * 20
                    norm_y = (0.5 - y / h) * 20 
                    norm_z = ((255 - avg_brightness) / 255) * self.depth_factor

                    if self.edge_detection and edges_gray is not None and np.mean(edges_gray[y:y_end, x:x_end]) > 50:
                        self.objects.append(Triangles([norm_x, norm_y, 0], max(0.5, depth/5), color_hex))
                    else:
                        size = max(0.2, min(1.0, cell_size / max_dim * 20))  
                        self.objects.append(Cube([norm_x, norm_y, norm_z/2], size, color_hex))

        return self.objects