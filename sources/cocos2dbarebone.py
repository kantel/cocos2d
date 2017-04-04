import cocos
from cocos.director import director 
from cocos.scene import Scene
from cocos.text import Label
from cocos.layer import Layer

class HelloWorld(Layer):                              
     def __init__(self):                               
         super(HelloWorld, self).__init__()            
         hello_world_label = Label(                    
             "Hallo Jörg!",                           
             font_name = "Times New Roman",            
             font_size = 32,                           
             anchor_x = 'center',                      
             anchor_y = 'center'                       
         )                                             
         hello_world_label.position = 160, 120         
         self.add(hello_world_label)    

def main():
    director.init(caption = "Hello World!", width = 320, height = 240)
    scene = Scene(HelloWorld())
    director.run(scene)

if __name__ == "__main__":
    main()