from pyray import *
from raylib import *
from random import randint

class Egg_Obstacle:
    def __init__(self, min_pos, max_pos, size, color):
        self.size = size
        self.color = color
        self.min_pos = Vector2(min_pos.x / size.x, min_pos.y / size.y)
        self.max_pos = Vector2(max_pos.x / size.x, max_pos.y / size.y)
        self.position = self.reloc_position()

    def reloc_position(self):
        x = randint(int(self.min_pos.x), int(self.max_pos.x) - 1)
        y = randint(int(self.min_pos.y), int(self.max_pos.y) - 1)
        vec = Vector2(x * self.size.x, y * self.size.y)
        return vec

    def draw(self):
        draw_rectangle_v(self.position, self.size, self.color)

    
    
        
