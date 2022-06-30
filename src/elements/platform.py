from raylib import *
from pyray import Rectangle
from .wall import Wall
from .ceiling import Ceiling

class Platform:
    def __init__(self, posx: int, posy: int, width: int, height: int, color: list[int]):
        self.rect = Rectangle(posx,posy,width,height)
        self.ceilingRect = Ceiling(posx, posy + height / 4, width, height/4, [200,200,200,255])
        self.color = color
    
    def draw(self):
        DrawRectangleRec(self.rect, self.color)

    def collision(self, player) -> bool:
        if CheckCollisionRecs(self.rect, player):
            return True
        else:
            return False