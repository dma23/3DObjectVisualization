from objects import Cube
import random 


class ObjectGenerator:
    
    def __init__(self): 
        self.object_type = Cube
        self.colours = ['red', 'blue', 'green', 'purple', 'orange']

    def generate_object(self): 

        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        z = random.uniform(-100, 100)

        center = [x, y, z]

        size = random.uniform(-15, 15)
        colour = random.choice(self.colours)
        obj_type = Cube

        return obj_type(center, size, colour)