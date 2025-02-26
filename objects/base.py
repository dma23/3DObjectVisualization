from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Object3D:
     
    def __init__(self, center, size, colour):
        self.center = center
        self.size = size
        self.colour = colour

        self.vertices = None
        self.faces = None
        self.generate_basic()


    def generate_basic(self):

        pass 

    
    def get_collection(self, edges=''):

        if self.vertices is None or self.faces is None:
            return None
        
        face_vertices = [[self.vertices[i] for i in face] for face in self.faces]
        collection = Poly3DCollection(face_vertices, alpha=0.8, linewidths=0.1, edgecolors='black')
        collection.set_facecolor(self.colour)
        return collection