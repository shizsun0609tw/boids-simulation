import pyglet
import graphics as g
import boids as b
import camera as c
import gui as u
import obstacle as o

#import ei.patched

def setup():
    print('======================')
    print('==       setup      ==')
    print('======================')

    c.setup()
    b.setup()
    g.setup()
    u.setup()
    o.setup()

def mainloop():
    print('======================')
    print('==     mainloop     ==')
    print('======================')

    g.event_func()
    pyglet.clock.schedule(b.update)

    pyglet.app.run()

def run():
    print('\n==============================')
    print('Start to run boids simulation')
    print('==============================\n')

    setup()
    mainloop()