import cocos
from cocos.director import director 
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.sprite import Sprite

import cocos.collision_model as cm
import cocos.euclid as eu

from collections import defaultdict
from pyglet.window import key

class Actor(Sprite):
    
    def __init__(self, x, y, pic):
        super(Actor, self).__init__(pic)
        self.position = pos = eu.Vector2(x, y)
        self.cshape = cm.CircleShape(pos, self.width/2)

class Game(ColorLayer):
    
    is_event_handler = True
    
    def __init__(self):
        super(Game, self).__init__(0, 80, 125, 255)
        
        self.heart_pic = "assets/heart.png"
        for pos in [(100, 100), (540, 380), (540, 100), (100, 380)]:
            self.add(Actor(pos[0], pos[1], self.heart_pic))
        self.player = Actor(320, 240, "assets/horngirl.png")
        self.add(self.player)
        
        cell = self.player.width * 1.25
        self.collman = cm.CollisionManagerGrid(0, 640, 0, 480, cell, cell)
        
        self.speed = 100.0
        self.pressed = defaultdict(int)
        self.schedule(self.update)
    
    def on_key_press(self, k, m):
        self.pressed[k] = 1
    
    def on_key_release(self, k, m):
        self.pressed[k] = 0
    
    def update(self, dt):
        # print(dt)
        self.collman.clear()
        for _, node in self.children:
            self.collman.add(node)
        for other in self.collman.iter_colliding(self.player):
            self.remove(other)
        
        x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
        y = self.pressed[key.UP] - self.pressed[key.DOWN]
        if (x != 0) or (y != 0):
            pos = self.player.position
            new_x = pos[0] + self.speed * x * dt
            new_y = pos[1] + self.speed * y * dt
            self.player.position = (new_x, new_y)
            self.player.cshape.center = self.player.position

def main():
    director.init(caption = "Kitty sammelt Herzen", width = 640, height = 480)
    scene = Scene(Game())
    director.run(scene)

if __name__ == "__main__":
    main()