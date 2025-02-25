from .base import Object3D

class Cube(Object3D):

    def generate_basic(self): 
        size = self.size / 2 
        cx, cy, cz = self.center

        self.verticesize = [
            [cx-size, cy-size, cz-size], [cx+size, cy-size, cz-size], [cx+size, cy+size, cz-size], [cx-size, cy+size, cz-size],
            [cx-size, cy-size, cz+size], [cx+size, cy-size, cz+size], [cx+size, cy+size, cz+size], [cx-size, cy+size, cz+size]
        ]

        self.faces = [
            [0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4],
            [1, 2, 6, 5], [2, 3, 7, 6], [3, 0, 4, 7]
        ]