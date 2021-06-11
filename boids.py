import math
import random
from pyglet.gl import *

class Boid:
    def __init__(self):
        self.position = [0.0, 0.0, 0.0]
        self.rotation = [0.0, 0.0, 0.0]
        self.velocity = [0.0, 0.0, 0.0]
        self.color = [0, 0, 1]
        self.bound = [5, 5, 5]

def setup():
    member_num = 50

    global boid

    print('Start to setup boids ...', end=' ')
    random.seed(0)
    boid = [Boid() for i in range(member_num)]

    for i in range(len(boid)):
        for j in range(3):
            boid[i].position[j] = random.randrange(-50, 50) / 10
            boid[i].velocity[j] = random.randrange(-10, 10) / 10

    print('  Finished!\n')

def draw_boid_unit():
    vertex = [[[0.1, 0, 0], [-0.2, 0.1, -0.1], [-0.2, 0.1, 0.1]],
        [[ 0.1,   0,   0], [-0.2,  0.1,  0.1], [-0.2, -0.1,    0]],
        [[ 0.1,   0,   0], [-0.2, -0.1,    0], [-0.2,  0.1, -0.1]],
        [[-0.2, 0.1, 0.1], [-0.2, 0.1, -0.1], [-0.2, -0.1,   0]]]
    # forward x

    for i in range(len(vertex)):
        glBegin(GL_TRIANGLES)
        for j in range(3):
            glVertex3f(*vertex[i][j])
        glEnd()

def draw():
    global boid

    for i in range(len(boid)):
        glPushMatrix()

        glTranslatef(boid[i].position[0], boid[i].position[1], boid[i].position[2])
        glRotatef(boid[i].rotation[0], 1, 0, 0)
        glRotatef(boid[i].rotation[1], 0, 1, 0)
        glRotatef(boid[i].rotation[2], 0, 0, 1)
        
        glColor3f(*boid[i].color)
        draw_boid_unit()
        glPopMatrix()

def update(delta_time):
    global boid

    fixed_dis = 0.5
    for i in range(len(boid)):
        for j in range(3):
            boid[i].position[j] += delta_time * boid[i].velocity[j]
            if boid[i].position[j] >= boid[i].bound[j]:
                boid[i].position[j] = boid[i].bound[j] - fixed_dis
                boid[i].velocity[j] *= -1
            elif boid[i].position[j] <= -boid[i].bound[j]:
                boid[i].position[j] = -boid[i].bound[j] + fixed_dis
                boid[i].velocity[j] *= -1