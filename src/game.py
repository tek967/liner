from raylib import *
from character.player import Player
from pyray import Camera2D
from config.fetch import loadConfig
from elements import platform, ceiling
from elements.wall import Wall
from gameio.dataio import *

"""
Liner: a 2d platformer game written in raylib and python. (meow)
"""

class Game:
    def __init__(self) -> None:
        self.version = 'alpha 1.0 bringup 6'
        self.palette = getPalette()
        self.config = loadConfig()
        self.width, self.height, self.fps, self.title = self.config['screen_width'], self.config['screen_height'], self.config['fps_clock'], bytes(self.config['title'], 'utf-8')
        self.player = Player()
        self.camera = Camera2D()
        self.camera.offset = self.width/2, self.height/2
        self.camera.rotation = 0.0
        self.camera.zoom = self.config['camera_zoom']
        self.walls, self.platforms = getMap()
        self.ceilings = [platform.ceilingRect for platform in self.platforms]
        self.ceilings.insert(0, ceiling.Ceiling(-210,-200,1000,10,[255,0,0,255]))
        
        InitWindow(self.width, self.height, self.title)
        SetTargetFPS(self.fps)
        while not WindowShouldClose(): 
            self.update()

    def checkPlatformCollision(self, platform):
            if platform.collision(self.player.rect):
                if self.player.rect.x < platform.rect.x + platform.rect.width and self.player.rect.x + self.player.rect.width > platform.rect.x:
                    self.player.floorHeight = platform.rect.y - self.player.rect.height
            else:
                for p in self.platforms:
                    if self.player.rect.x < p.rect.x + p.rect.width and self.player.rect.x + self.player.rect.width > p.rect.x:
                        if p.rect.y > self.player.rect.y:
                            self.player.floorHeight = p.rect.y - self.player.rect.height
    
    def checkCeilingCollision(self, ceiling):
        if ceiling.isPlayerUnder(self.player):
            self.player.ceilingHeight = ceiling.rect.y + ceiling.rect.height
        else:
            for c in self.ceilings:
                if c.isPlayerUnder(self.player):
                    self.player.ceilingHeight = c.rect.y + c.rect.height


    def update(self):
        for ceiling in self.ceilings:
            self.checkCeilingCollision(ceiling)
        for wall in self.walls:
            wall.collision(self.player)
        self.player.update()
        for platform in self.platforms:
            self.checkPlatformCollision(platform)
        BeginDrawing()
        self.camera.target = self.player.rect.x + self.player.rect.width/2, self.player.rect.y + self.player.rect.height/2
        self.draw()
        EndDrawing()

    def draw(self):
        ClearBackground([240,240,240,255])
        DrawText(bytes(self.version, 'utf-8'), 20, 20, 20, self.palette['navy'])
        if self.config['debug_enable']:
            DrawText(bytes(f"XY: {round(self.player.rect.x,2)},{round(self.player.rect.y,2)}",'utf-8'), 20, 45, 15, self.palette['gray'])
            DrawText(bytes(f'XY Velocity: {round(self.player.velocity.x,1)},{round(self.player.velocity.y,1)}','utf-8'), 20, 60, 15, self.palette['gray'])
            DrawText(bytes(f'Jump Tick Timer: {self.player.jumpTickTimer}, Stop Incrementing Jump Tick Timer: {self.player.stopIncrementingJumpTickTimer}', 'utf-8'), 20, 75, 15, self.palette['gray'])
            DrawText(bytes(f"Floor height: {self.player.floorHeight}", 'utf-8'), 20, 90, 15, self.palette['gray'])
            DrawText(bytes(f"Health: {self.player.health}", 'utf-8'),20, 105, 15,self.palette['gray'])
        if self.config['show_meow_in_credits']:
            DrawText(b"by easontek2398 and meowscripty (meow~)",20,self.height - 50,15,self.palette["lightblue"])
        else:
            DrawText(b'by easontek2398 and meowscripty',20, self.height - 50, 15, self.palette('blue'))
        BeginMode2D(self.camera)
        self.player.draw()

        for wall in self.walls:
            wall.draw()

        for ceil in self.ceilings:
            ceil.draw()
        
        for platform in self.platforms:
            platform.draw()
        EndMode2D()