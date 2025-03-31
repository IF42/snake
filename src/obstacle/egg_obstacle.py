from pyray import *
from raylib import *
from random import randint


class Egg_Obstacle:
    def __init__(self, min_pos, max_pos, size, color):
        self.size = size
        self.color = color
        self.min_pos = min_pos
        self.max_pos = max_pos
        self.position = self.reloc_position()

    def reloc_position(self):
        x = randint(int(self.min_pos.x / self.size.x), int((self.max_pos.x - self.size.x) / self.size.x) - 2)
        y = randint(int(self.min_pos.y / self.size.y), int((self.max_pos.y - self.size.y) / self.size.y) - 2)
        vec = Vector2(self.min_pos.x + (x * self.size.x), self.min_pos.y + (y * self.size.y))
        return vec

    def draw(self):
        draw_rectangle_v(self.position, self.size, self.color)

    
    
        
