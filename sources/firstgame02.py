import cocos
from cocos.director import director 
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.sprite import Sprite

from collections import defaultdict
from pyglet.window import key

class Game(ColorLayer):
    
    is_event_handler = True
    
    def __init__(self):
        super(Game, self).__init__(0, 80, 125, 255)
        self.player = Sprite("assets/horngirl.png")
        self.player.position = 320, 240
        self.add(self.player)
        
        self.speed = 100.0
        self.pressed = defaultdict(int)
        self.schedule(self.update)
    
    def on_key_press(self, k, m):
        self.pressed[k] = 1
    
    def on_key_release(self, k, m):
        self.pressed[k] = 0
    
    def update(self, dt):
        x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
        y = self.pressed[key.UP] - self.pressed[key.DOWN]
        if (x != 0) or (y != 0):
            pos = self.player.position
            new_x = pos[0] + self.speed * x * dt
            new_y = pos[1] + self.speed * y * dt
            self.player.position = (new_x, new_y)

def main():
    director.init(caption = "Moving Kitty", width = 640, height = 480)
    scene = Scene(Game())
    director.run(scene)

if __name__ == "__main__":
    main()