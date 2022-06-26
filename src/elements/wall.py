from raylib import *
from pyray import Rectangle

class Wall:
    def __init__(self, posx, posy, width, height, color):
        self.leftRect = Rectangle(posx,posy,width/2,height)
        self.rightRect = Rectangle(posx+width/2,posy,width/2,height)
        self.color = color
    def draw(self):
        DrawRectangleRec(self.leftRect,self.color)
        DrawRectangleRec(self.rightRect,self.color)
    def collision(self, player):
        if CheckCollisionRecs(self.leftRect, player.rect):
            player.velocity.x = 0
            player.rect.x = self.leftRect.x - player.rect.width
        if CheckCollisionRecs(self.rightRect, player.rect):
            player.velocity.x = 0
            player.rect.x = self.rightRect.x + self.rightRect.width