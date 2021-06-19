import math
import numpy as np
from copy import *

def distance(v1, v2):
    if len(v1) != len(v2):
        print('distance len error')
        return -1

    return math.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(v1, v2)))

def dot(v1, v2):
    return sum(i * j for i, j in zip(v1, v2))

def magnitude(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)

def normalized(v):
    return [i / magnitude(v) for i in v]

def limit_velocity(v, max_v, min_v):
    mag = magnitude(v)
    
    if mag > max_v:
        return [v[i] * (max_v / mag) for i in range(3)]
    elif mag < min_v:
        return [v[i] * (min_v / mag) for i in range(3)]
    else:
        return v