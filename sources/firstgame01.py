import cocos
from cocos.director import director 
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
from pyglet.window import key

class Game(ColorLayer):
    
    is_event_handler = True
    
    def __init__(self):
        super(Game, self).__init__(0, 80, 125, 255)
        self.player = Sprite("assets/horngirl.png")
        self.player.position = 320, 240
        self.add(self.player)
    
    def on_key_press(self, k, m):
        print("Pressed", key.symbol_string(k))
    
    def on_key_release(self, k, m):
        print("Released", key.symbol_string(k))

def main():
    director.init(caption = "Moving Kitty", width = 640, height = 480)
    scene = Scene(Game())
    director.run(scene)

if __name__ == "__main__":
    main()