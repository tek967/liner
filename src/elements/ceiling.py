from raylib import *
from pyray import Rectangle

class Ceiling:
    def __init__(self, posx:int, posy:int, width:int, height:int, color:list[int]) -> None:
        self.rect = Rectangle(posx, posy, width, height)
        self.color = color

    def draw(self):
        DrawRectangleRec(self.rect, self.color)

    def collision(self, player):
        if player.rect.x < self.rect.x + self.rect.width and player.rect.x + player.rect.width > self.rect.x and player.rect.y > self.rect.y + self.rect.height:
            player.ceilingHeight = self.rect.y + self.rect.height