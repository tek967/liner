from raylib import *
from pyray import Rectangle

class Wall:
    def __init__(self, posx: int, posy: int, width: int, height:int, color: list[int], allowJumpingPass: bool):
        self.leftRect = Rectangle(posx,posy,width/2,height)
        self.rightRect = Rectangle(posx+width/2,posy,width/2,height)
        self.color = color
        self.allowJumpingPass = allowJumpingPass
    def draw(self):
        DrawRectangleRec(self.leftRect,self.color)
        DrawRectangleRec(self.rightRect,self.color)
    def collision(self, player):
        if self.allowJumpingPass:
            if player.velocity.x != 0 and player.velocity.y > -0.3:
                if CheckCollisionRecs(self.leftRect, player.rect):
                    player.velocity.x = 0
                    player.rect.x = self.leftRect.x - player.rect.width
                if CheckCollisionRecs(self.rightRect, player.rect):
                    player.velocity.x = 0
                    player.rect.x = self.rightRect.x + self.rightRect.width
        else: 
            if player.velocity.x != 0:
                if CheckCollisionRecs(self.leftRect, player.rect):
                    player.velocity.x = 0
                    player.rect.x = self.leftRect.x - player.rect.width
                if CheckCollisionRecs(self.rightRect, player.rect):
                    player.velocity.x = 0
                    player.rect.x = self.rightRect.x + self.rightRect.width