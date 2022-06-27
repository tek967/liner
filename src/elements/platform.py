from raylib import *
from pyray import Rectangle
from .wall import Wall

class Platform:
    def __init__(self, posx: int, posy: int, width: int, height: int, color: list[int]):
        self.rect = Rectangle(posx,posy,width,height)
        self.color = color
    
    def draw(self):
        DrawRectangleRec(self.rect, self.color)

    def collision(self, player) -> bool:
        if CheckCollisionRecs(self.rect, player):
            return True
        else:
            return False