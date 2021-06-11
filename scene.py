import math
from pyglet.gl import *

def setup():
    pass

def render_ground():
    glPushMatrix()

    glTranslatef(-5.5, -5, -4.5)
    for i in range(10):
        for j in range(10):
            if (i + j) % 2 == 0:
                glColor3f(0, 0, 0)
            else:
                glColor3f(1, 1, 1)

            glTranslatef(1, 0, 0)

            glBegin(GL_POLYGON)
            glVertex3f(-0.5, 0, -0.5)
            glVertex3f(-0.5, 0, 0.5)
            glVertex3f(0.5, 0, 0.5)
            glVertex3f(0.5, 0, -0.5)
            glEnd()

        glTranslatef(-10, 0, 1)

    glPopMatrix()
    

def render_bound():
    bound = [[[-5, 5, -5], [-5, 5, 5]],
        [[-5,  5,  5], [ 5,  5,  5]],
        [[ 5,  5,  5], [ 5,  5, -5]],
        [[ 5,  5, -5], [-5,  5, -5]],
        [[-5,  5,  5], [-5, -5,  5]],
        [[ 5,  5,  5], [ 5, -5,  5]],
        [[ 5,  5, -5], [ 5, -5, -5]],
        [[-5,  5, -5], [-5, -5, -5]],
        [[-5, -5, -5], [-5, -5,  5]],
        [[-5, -5,  5], [ 5, -5,  5]],
        [[ 5, -5,  5], [ 5, -5, -5]],
        [[ 5, -5, -5], [-5, -5, -5]]]

    glColor3f(1, 0, 0)
    glPushMatrix()
    for i in range(len(bound)):
        glBegin(GL_LINES)
        glVertex3f(*bound[i][0])
        glVertex3f(*bound[i][1])
        glEnd()
    glPopMatrix()

def draw():
    render_ground()
    render_bound()