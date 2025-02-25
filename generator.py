from objects import Cube
import random 


class ObjectGenerator:
    
    def __init__(self): 
        self.object_type = Cube
        self.colours = ['red', 'blue', 'green']

    def generate_object(self): 

        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)
        z = random.uniform(-2, 2)

        center = [x, y, z]

        size = random.uniform(-2, 2)
        colour = random.choice(self.colours)
        obj_type = Cube

        return obj_type(center, size, colour)