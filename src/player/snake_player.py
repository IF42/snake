from pyray import *
from raylib import *

class Snake_Player:
    def __init__(self, position, size, color):
        self.default_position = position
        self.node_chain = [position]
        self.size = size
        self.color = color
        self.direction = Vector2(0, 0)
        self.append_request = False

    def append_node(self):
        self.append_request = True

    def turn_right(self):
        if self.direction.x != -1:
            self.direction = Vector2(1, 0)
        
    def turn_left(self):
        if self.direction.x != 1:
            self.direction = Vector2(-1, 0)

    def turn_up(self):
        if self.direction.y != 1:
            self.direction = Vector2(0, -1)

    def turn_down(self):
        if self.direction.y != -1:
            self.direction = Vector2(0, 1)

    def head_position(self):
        return self.node_chain[0]

    def reset(self):
        self.node_chain.clear()
        self.direction = Vector2(0, 0)
        self.node_chain.append(self.default_position)

    def move(self):
        head = Vector2(
                self.node_chain[0].x + (self.direction.x * self.size.x)
                , self.node_chain[0].y + (self.direction.y * self.size.y))

        self.node_chain.insert(0, head)

        if self.append_request == False:
            self.node_chain.pop()
        else:
            self.append_request = False
        
    def draw(self):
        for node in self.node_chain:
            draw_rectangle_v(node, self.size, self.color)





