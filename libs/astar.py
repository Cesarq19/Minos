import time
import headp

class Node(self):
    def __init__(self, x, y, g, h, parent):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def heuristic(node,goal):
        return ((node.x - goal.x) ** 2 + (node.y - goal.y) ** 2) **0.5

