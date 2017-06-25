from collections import defaultdict
from pyglet.window import key

from cocos.director import director 
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.sprite import Sprite
import cocos.collision_model as cm
import cocos.euclid as eu

class Actor(Sprite):
    
    def __init__ (self, image, x, y):
        super(Actor, self).__init__(image)
        self.position = eu.Vector2(x, y)
        self.cshape = cm.AARectShape(self.position, self.width*0.5, self.height*0.5)
        
    def move(self, offset):
        self.position += offset
        self.cshape.center += offset
    
    def update(self, elapsed):
        pass
        
    def collide(self, other):
        pass

class PlayerCannon(Actor):
    
    KEYS_PRESSED = defaultdict(int)
    
    def __init__(self, x, y):
        super(PlayerCannon, self).__init__("images/cannon.png", x, y)
        self.speed = eu.Vector2(200, 0)
    
    def update(self, elapsed):
        pressed = PlayerCannon.KEYS_PRESSED
        movement = pressed[key.RIGHT] - pressed[key.LEFT]
        w = self.width*0.5
        if movement != 0: # and w <= self.x <= self.parent.width - w:
            self.move(self.speed*movement*elapsed)
    
    def collide(self, other):
        other.kill()
        self.kill()

class GameLayer(Layer):
    
    is_event_handler = True
    
    def on_key_press(self, k, _):
        PlayerCannon.KEYS_PRESSED[k] = 1
    
    def on_key_release(self, k, _):
        PlayerCannon.KEYS_PRESSED[k]= 0
    
    def __init__(self):
        super(GameLayer, self).__init__()
        w, h = director.get_window_size()
        self.width = w
        self.height = h
        self.lives = 3
        self.score = 0
        self.update_score()
        self.create_player()
        self.create_alien_group(100, 300)
        cell = 1.25*50
        self.collman = cm.CollisionManagerGrid(0, w, 0, h, cell, cell)
        self.schedule(self.update)
    
    def create_player(self):
        self.player = PlayerCannon(self.width*0.5, 50)
        self.add(self.player)
    
    def update_score(self, score = 0):
        self.score += score
    
    def create_alien_group(self, x, y):
        pass
    
    def update(self, dt):
        self.collman.clear()
        for _, node in self.children:
            self.collman.add(node)
            if not self.collman.knows(node):
                self.remove(node)
        for _, node in self.children:
            node.update(dt)
    
    def collide(self, node):
        if node is not None:
            for other in self.collman.iter_colliding(node):
                node.collide(other)
                return True
        return False

def main():
    director.init(caption = "Cocos Invaders", width = 800, height = 650)
    game_layer = GameLayer()
    main_scene = Scene(game_layer)
    director.run(main_scene)
    
if __name__ == "__main__":
    main()