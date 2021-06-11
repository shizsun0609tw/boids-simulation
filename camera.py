from pyglet.gl import *

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 8

        self.x_rot = 0
        self.y_rot = 0
        self.z_rot = 0

def setup():
    print('Start to setup graphics ...', end=' ')

    global camera
    camera = Camera()
    
    print('  Finished!\n')

def update_translate(translate):
    camera.x += translate[0]
    camera.y += translate[1]
    camera.z += translate[2]
    
def update_rotate(rotate):
    camera.x_rot += rotate[0]
    camera.y_rot += rotate[1]
    camera.z_rot += rotate[2]
    
def apply():
    glTranslatef(-camera.x, -camera.y, -camera.z)

    glRotatef(camera.x_rot, 1, 0, 0)
    glRotatef(camera.y_rot, 0, 1, 0)
    glRotatef(camera.z_rot, 0, 0, 1)