import math
import my_math
import random
import numpy as np
from pyglet.gl import *
from mathutils import Vector

BOID_NEARBY_THRESH = 2
BOID_SEPARATION_DIS = 0.75
BOID_MAX_VELOCITY = 3
BOID_MIN_VELOCITY = 1

BOID_TRACK_DIS = 0.3

cohesion_factor = 0.03
separation_factor = 0.25
alignment_factor = 0.045

class Boid:
    def __init__(self):
        self.position = [0.0, 0.0, 0.0]
        self.velocity = [0.0, 0.0, 0.0]
        self.acceleration = [0.0, 0.0, 0.0]
        self.color = [0, 0, 1]
        self.bound = [5, 5, 5]
        self.tracker = []
        self.time = 0

def setup():
    member_num = 20

    global boid

    print('Start to setup boids ...', end=' ')
    random.seed(0)
    boid = [Boid() for i in range(member_num)]

    for i in range(len(boid)):
        for j in range(3):
            boid[i].position[j] = random.randrange(-50000, 50000) / 10000
            boid[i].velocity[j] = random.randrange(-30000, 30000) / 10000
    print('  Finished!\n')

def draw_boid_unit():
    glColor3f(0, 0, 1)
    sphere = gluNewQuadric()
    gluSphere(sphere, 0.25, 10, 10)

def draw_boid_tracker(boid_unit):
    glColor3f(0.8, 0.8, 0.5)
    glPointSize(2.5)
    for t in boid_unit.tracker:
        glBegin(GL_POINTS)
        glVertex3f(*[t[i] - boid_unit.position[i] for i in range(3)])
        glEnd()

def draw_foward(boid_unit):
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    forward = [my_math.normalized(boid_unit.velocity)[j] for j in range(3)]
    glVertex3f(*forward)
    glEnd()

def draw():
    global boid

    for i in range(len(boid)):
        glPushMatrix()

        glTranslatef(boid[i].position[0], boid[i].position[1], boid[i].position[2])

        #draw_foward(boid[i])
        draw_boid_tracker(boid[i])
        draw_boid_unit()

        glPopMatrix()

def cal_nearby_boids(target_boid):
    global boid
    
    res = []
    for boid_unit in boid:
        if boid_unit == target_boid:
            continue
        else:
            dis = my_math.distance(target_boid.position, boid_unit.position)
            
            if dis < BOID_NEARBY_THRESH:
                res.append(boid_unit)

    return res    

def cal_cohesion(target_boid, nearby_boids):
    # rule 1
    sum = [0, 0, 0]
    for boid_unit in nearby_boids:
        sum = [sum[i] + boid_unit.position[i] for i in range(3)]

    avg_position = [sum[i] / len(nearby_boids) for i in range(3)]
    
    return [avg_position[i] - target_boid.position[i] for i in range(3)]

def cal_separation(target_boid, nearby_boids):
    # rule 2
    c = [0, 0, 0]
    for boid_unit in nearby_boids:
        if my_math.distance(boid_unit.position, target_boid.position) < BOID_SEPARATION_DIS:
            c = [c[i] - (boid_unit.position[i] - target_boid.position[i]) for i in range(3)]

    return c

def cal_alignment(target_boid, nearby_boids):
    # rule 3
    sum = [0, 0, 0]
    for boid_unit in nearby_boids:
        sum = [sum[i] + boid_unit.velocity[i] for i in range(3)]

    avg_velocity = [sum[i] / len(nearby_boids) for i in range(3)]

    return [avg_velocity[i] - target_boid.velocity[i] for i in range(3)]

def append_tracker(boid_unit):
    tracker_num = 5
    if len(boid_unit.tracker) > 5:
        boid_unit.tracker.pop(0)
    
    boid_unit.tracker.append(boid_unit.position)

def update(delta_time):
    global boid

    for i in range(len(boid)):
        nearby_boids = cal_nearby_boids(boid[i])

        if len(nearby_boids) == 0:
            boid[i].acceleration = [0, 0, 0]
        else:
            cohesion = cal_cohesion(boid[i], nearby_boids)
            separation = cal_separation(boid[i], nearby_boids)
            alignment = cal_alignment(boid[i], nearby_boids)

            boid[i].acceleration =  \
                [ cohesion_factor   * cohesion[i] 
                + separation_factor * separation[i] 
                + alignment_factor  * alignment[i] for i in range(3)]

    fixed_dis = 0.5
    for i in range(len(boid)):
        boid[i].time += delta_time

        if boid[i].time >= BOID_TRACK_DIS:
            boid[i].time = 0
            append_tracker(boid[i])

        boid[i].velocity = [boid[i].velocity[j] + boid[i].acceleration[j] for j in range(3)]
        my_math.limit_velocity(boid[i].velocity, BOID_MAX_VELOCITY, BOID_MIN_VELOCITY)

        boid[i].position = [boid[i].position[j] + delta_time * boid[i].velocity[j] for j in range(3)]

        for j in range(3):
            if boid[i].position[j] >= boid[i].bound[j]:
                boid[i].position[j] = boid[i].bound[j] - fixed_dis
                boid[i].velocity[j] *= -1
            elif boid[i].position[j] <= -boid[i].bound[j]:
                boid[i].position[j] = -boid[i].bound[j] + fixed_dis
                boid[i].velocity[j] *= -1