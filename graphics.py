import pyglet
from pyglet.gl import *
from pyglet.window import key

import boids as b
import scene as s
import camera as c
import gui as u

def setup():
    print('Start to setup graphics ...', end=' ')

    global window
    window = pyglet.window.Window(
        fullscreen=False,
        caption="Boids Simulation",
        width=1280, height=960)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_CULL_FACE)
    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_POSITION, (GLfloat*4)(0.0, 0.0, 0.0, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT,  (GLfloat*4)(0.3, 0.3, 0.3, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  (GLfloat*4)(0.5, 0.5, 0.5, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (GLfloat*4)(1.0, 1.0, 1.0, 1))

    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)
    
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glLineWidth(2.0)

    print('  Finished!\n\n')

    print('=============================')
    print('Key input:')
    print('\t[W, S]: forward, backward')
    print('\t[A, D]: left, right')
    print('\t[Q, E]: pitch')
    print('\t[Z, C]: yaw')
    print('=============================')

def event_func():
    global window    

    @window.event
    def on_draw():
        window.clear()
        glClearColor(0.1, 0.1, 0.1, 1.0)

        glEnable(GL_DEPTH_TEST)
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(100, 1, 0.1, 100)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        c.apply()

        s.draw()
        b.draw()
        u.draw()
        
        glFlush()

    @window.event
    def on_key_press(signal, modifiers):
        if signal == key.W:
            c.update_translate([0, 0, -1])
        elif signal == key.A:
            c.update_translate([-1, 0, 0])
        elif signal == key.S:
            c.update_translate([0, 0, 1])
        elif signal == key.D:
            c.update_translate([1, 0, 0])
        elif signal == key.Q:
            c.update_rotate([3, 0, 0])
        elif signal == key.E:
            c.update_rotate([-3, 0 , 0])
        elif signal == key.Z:
            c.update_rotate([0, 3, 0])
        elif signal == key.C:
            c.update_rotate([0, -3, 0])

    @window.event
    def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        if buttons & pyglet.window.mouse.LEFT:
            u.handle_mouse(x, y, dx, dy)