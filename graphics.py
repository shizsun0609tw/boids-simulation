import pyglet
from pyglet.gl import *
from pyglet.window import key

import boids as b
import scene as s
import camera as c

def get_window_config():
    platform = pyglet.window.get_platform()
    display = platform.get_default_display()
    screen = display.get_default_screen()

    template = Config(double_buffer=True, sample_buffers=1, samples=4)

    try:
        config = screen.get_best_config(template)
    except pyglet.window.NoSuchConfigException:
        template = Config()
        config = screen.get_best_config(template)

    return config

def setup():
    print('Start to setup graphics ...', end=' ')

    global window
    window = pyglet.window.Window(
        fullscreen=False,
        caption="Boids Simulation",
        config=get_window_config())

    print('  Finished!\n')

def event_func():
    global window    

    @window.event
    def on_draw():
        window.clear()
        glClearColor(0.1, 0.1, 0.1, 1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(120, 1, 0.1, 100)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        c.apply()

        s.draw()
        b.draw()

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