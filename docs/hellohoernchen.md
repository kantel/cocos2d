# Hallo Hörnchen

In diesem zweiten Teil meiner kleinen Reihe, in der ich versuche, mir selber Cocos2d (Python) beizubringen, möchte ich das minimale Grundgerüst aus dem ersten Teil weiter aufbohren. Im Endeffekt soll so etwas herauskommen, wie mein [PyGame](http://cognitiones.kantel-chaos-team.de/multimedia/spieleprogrammierung/pygame.html)-Tutorial aus dem letzten Jahr ([Teil 1](http://blog.schockwellenreiter.de/2016/05/2016052001.html), [Teil 2](http://blog.schockwellenreiter.de/2016/05/2016052003.html), [Teil 3](http://blog.schockwellenreiter.de/2016/05/2016052405.html) und [Teil 4](http://blog.schockwellenreiter.de/2016/05/2016052606.html)), das ich ja auch schon erfolgreich nach [Processing.py](http://cognitiones.kantel-chaos-team.de/programmierung/creativecoding/processing/processingpy.html) portiert hatte ([Teil 1](http://blog.schockwellenreiter.de/2016/11/2016110703.html), [Teil 2](http://blog.schockwellenreiter.de/2016/11/2016110805.html), [Teil 3](http://blog.schockwellenreiter.de/2016/11/2016110904.html) und [Teil 4](http://blog.schockwellenreiter.de/2016/11/2016111203.html)). Nun also der Versuch mit Cocos2d:

![Hörnchen](images/hoernchen01.png)

Um dieses Bild zu erzeugen, habe ich den Quelltext des Grundgerüstes nur ein wenig aufgebohrt:

~~~python
import cocos
from cocos.director import director 
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.sprite import Sprite

class Game(ColorLayer):
    
    def __init__(self):
        super(Game, self).__init__(0, 80, 125, 255)
        self.player = Sprite("assets/horngirl.png")
        self.player.position = 160, 120
        self.add(self.player)

def main():
    director.init(caption = "Hello Hörnchen!", width = 320, height = 240)
    scene = Scene(Game())
    director.run(scene)

if __name__ == "__main__":
    main()
~~~

Die Klasse `Game` erbt von `ColorLayer`, der in der `__init__()`-Funktion eine Hintergrundfarbe im Format RGBA mitgegeben wird. Dann wird das Bild der jungen Dame geladen und positioniert. In der `main()`-Funktion wird die Scene geladen und angezeigt. Das ist alles, aber es geht noch mehr.

In einer zweiten Version habe ich ein Modul `resources.py` angelegt

~~~python
import pyglet

pyglet.resource.path = ["assets"]
pyglet.resource.reindex()

horngirl = pyglet.resource.image("horngirl.png")
~~~

und dort das Hörnchen versteckt. Damit kann man es sich im Hauptprogramm – besonders wenn man viele resourcen hat – noch einfacher machen:

~~~python
import cocos
from cocos.director import director 
from cocos.scene import Scene
from cocos.layer import ColorLayer
from cocos.sprite import Sprite
import resources

class Game(ColorLayer):
    
    def __init__(self):
        super(Game, self).__init__(0, 80, 125, 255)
        self.player = Sprite(resources.horngirl)
        self.player.position = 160, 120
        self.add(self.player)

def main():
    director.init(caption = "Hello Hörnchen!", width = 320, height = 240)
    scene = Scene(Game())
    director.run(scene)

if __name__ == "__main__":
    main()
~~~

Cocos2d setzt ja bekanntlich auf PyGlet auf und warum soll man dann nicht PyGlet die Ressourcenverwaltung überlassen? Bei nur einer Ressource ist es eher Mehraufwand, aber bei vielen Ressourcen kann sich das durchaus auszahlen. *Still digging!*

