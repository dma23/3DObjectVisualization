from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Object3D:
     
    def __init__(self, center, size, colour):
        self.center = center
        self.size = size
        self.colour = colour

        self.vertices = None
        self.faces = None
    
