from objects.shapes import Cube

class figure:

    def __init__(self): 
        
        self.colours = {
            'skin': '#c18c69',      
            'hair': '#3b2616',      
            'eyes': '#000000',      
            'mouth': '#6b4431',     
            'shirt': '#3056bf',     
            'pants': '#215b31',     
            'shoes': '#3d3d3d',     
            'belt': '#2b2b2b',      
            'sleeve': '#2a4dac'    
        }

        self.scale = 1.5
        self.cubes = [] 

    
    def build(self):

        self.cubes = []

        self._add_head(20, 15, 22)
        
        self._add_torso(20, 15, 14)
        
        self._add_arm(16, 15, 14, 'left')
        self._add_arm(24, 15, 14, 'right')
        
        self._add_leg(21.5, 15, 3, 'left')
        self._add_leg(18.5, 15, 3, 'right')

        return self.cubes

    def _add_head(self, x, y, z):

        for dx in range(-2, 2):
            for dy in range(-2, 2):
                for dz in range(-2, 2):
                    pos_x = x + dx * self.scale
                    pos_y = y + dz * self.scale
                    pos_z = z + dy * self.scale
                    
                    if dy == 1:  
                        colour = self.colours['hair']
                    else:
                        colour = self.colours['skin']
                    
                    self.cubes.append(Cube([pos_x, pos_y, pos_z], self.scale, colour))


    def _add_torso(self, x, y, z):

        for dx in range(-2, 2):
            for dy in range(-4, 4):
                for dz in range(-1, 1):
                    pos_x = x + dx * self.scale
                    pos_y = y + dz * self.scale
                    pos_z = z + dy * self.scale

                    if dy < -3:
                        colour = self.colours['belt']
                    else:
                        colour = self.colours['shirt']
                    
                    self.cubes.append(Cube([pos_x, pos_y, pos_z], self.scale, colour))
    

    def _add_arm(self, x, y, z, side):

        x_offset = 0 if side == 'left' else 0
        
        for dx in range(-1, 1):
            for dy in range(-3, 3):
                for dz in range(-1, 1):
                    pos_x = x + dx * self.scale + x_offset
                    pos_y = y + dz * self.scale
                    pos_z = z + dy * self.scale
                    
                    if dy < 0: 
                        colour = self.colours['skin']
                    else:  
                        colour = self.colours['sleeve']
                    
                    self.cubes.append(Cube([pos_x, pos_y, pos_z], self.scale, colour))
    

    def _add_leg(self, x, y, z, side):


        for dx in range(-1, 1):
            for dy in range(-3, 3):
                for dz in range(-1, 1):
                    pos_x = x + dx * self.scale
                    pos_y = y + dz * self.scale
                    pos_z = z + dy * self.scale
                    
                    if dy < -2:  
                        colour = self.colours['shoes']
                    else: 
                        colour = self.colours['pants']
                    
                    self.cubes.append(Cube([pos_x, pos_y, pos_z], self.scale, colour))