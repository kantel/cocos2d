import cocos
from cocos.director import director 
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
import resources

class Game(ColorLayer):
    
    def __init__(self):
        super(Game, self).__init__(102, 102, 225, 255)
        self.player = Sprite(resources.horngirl)
        self.player.position = 160, 120
        self.add(self.player)

def main():
    director.init(caption = "Hello Hörnchen!", width = 320, height = 240)
    scene = Scene(Game())
    director.run(scene)

if __name__ == "__main__":
    main()