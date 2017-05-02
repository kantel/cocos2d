import cocos
from cocos.director import director 
from cocos.scene import Scene
from cocos.layer import Layer
from cocos.sprite import Sprite


class MainLayer(Layer):
    
    def __init__(self):
        super(MainLayer, self).__init__()
        self.player = Sprite("assets/ball.png")
        self.player.color = (0, 0, 255)
        self.player.position = 320, 240
        self.add(self.player)

def main():
    director.init(caption = "Hallo Cocos2d!")
    scene = Scene(MainLayer())
    director.run(scene)

if __name__ == "__main__":
    main()