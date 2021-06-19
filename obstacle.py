import random
from pyglet.gl import *

class Obstacle():
    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size
        self.color = color

def setup():
    global obstacles
    obstacles = []
    obstacle_num = 10

    for i in range(obstacle_num):
        obstacles.append(
            Obstacle(
            [random.randrange(-50000, 50000) / 10000, random.randrange(-50000, 50000) / 10000, random.randrange(-50000, 50000) / 10000], 
            random.randrange(0, 10000) / 15000 + 0.3,
            [random.randrange(0, 100) / 100, random.randrange(0, 100) / 100, random.randrange(0, 100) / 100]))
    
def draw_cube():
    glBegin(GL_QUADS)
    glNormal3f(0, 1, 0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glNormal3f(0, -1, 0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glNormal3f(0, 0, 1)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glNormal3f(0, 0, -1)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glNormal3f(1, 0, 0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glNormal3f(-1, 0, 0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()

def draw():
    for obstacle in obstacles:
        glPushMatrix()
        glTranslatef(*obstacle.pos)
        glScalef(obstacle.size, obstacle.size, obstacle.size)
        glColor3f(*obstacle.color)

        draw_cube()

        glPopMatrix()

def get_obstacles():
    return obstacles