import math
from pyglet.gl import *

def setup():
    pass

def render_ground():
    glPushMatrix()

    glTranslatef(-5, -2, -5)
    for i in range(10):
        for j in range(10):
            if (i + j) % 2 == 0:
                glColor4f(0, 0, 0, 1)
            else:
                glColor4f(1, 1, 1, 0)

            glTranslatef(1, 0, 0)

            glBegin(GL_POLYGON)
            glVertex3f(-0.5, 0, -0.5)
            glVertex3f(-0.5, 0, 0.5)
            glVertex3f(0.5, 0, 0.5)
            glVertex3f(0.5, 0, -0.5)
            glEnd()

        glTranslatef(-10, 0, 1)

    glPopMatrix()
    

def draw():
    render_ground()