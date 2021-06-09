import pyglet
import graphics as g
import boids as b

def setup():
    print('======================')
    print('==       setup      ==')
    print('======================')

    b.setup()
    g.setup()

def mainloop():
    print('======================')
    print('==     mainloop     ==')
    print('======================')

    b.mainloop()
    g.mainloop()

    pyglet.app.run()

def run():
    print('\n==============================')
    print('Start to run boids simulation')
    print('==============================\n')

    setup()
    mainloop()