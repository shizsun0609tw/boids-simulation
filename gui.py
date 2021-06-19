import pyglet
from pyglet.gl import *

class ControlBar:
    def __init__(self, text, position, value, limit):
        self.text = text
        self.value = value
        self.position = position
        self.limit = limit
        self.bar_offset = 0
        self.bar_limit = 60

        self.text_label = pyglet.text.Label(
            text, font_name='Times New Roman', font_size=20, color=(0, 0, 0, 255),
            x=width//2 + position[0] - 75, y=height//2 + position[1], anchor_x='center', anchor_y='center')
        self.value_label = pyglet.text.Label(
            str(value), font_name='Times New Roman', font_size=15, color=(0, 0, 255, 255),
            x=width//2 + position[0] + 60, y=height//2 + position[1] - 35, anchor_x='center', anchor_y='center')

    def update_text(self):
        self.value_label = pyglet.text.Label(
            "{:.2f}".format(self.value), font_name='Times New Roman', font_size=20, color=(0, 0, 255, 255),
            x=width//2 + self.position[0] + 60, y=height//2 + self.position[1] - 35, anchor_x='center', anchor_y='center')

def setup():
    global width, height

    width = 1280
    height = 960

    global control_bar_list
    control_bar_list = []

    control_bar_list.append(ControlBar("Cohesion", [-450, -300], 0.03, [0.0, 0.06]))
    control_bar_list.append(ControlBar("Alignment", [-150, -300], 0.3, [0.0, 0.6]))
    control_bar_list.append(ControlBar('Separation', [150, -300], 0.1, [0.0, 0.2]))
    #control_bar_list.append(ControlBar('NULL', [450, -300], 0))
    
    control_bar_list.append(ControlBar('Min_V', [-450, -400], 2.5, [1, 4]))
    control_bar_list.append(ControlBar('Max_V', [-150, -400], 5, [4, 6]))
    control_bar_list.append(ControlBar('Nearby_dis', [150, -400], 1.25, [0, 2.5]))
    control_bar_list.append(ControlBar('Boids_dis', [450, -400], 1, [0, 2]))

def draw_widget(location_x, location_y, size_x, size_y, color):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-width//2, width//2, -height//2, height//2)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    glPushMatrix()
    glTranslatef(location_x, location_y, 0)
    glColor4f(*color)
    glBegin(GL_QUADS)
    glVertex2f(-size_x/2, size_y/2)
    glVertex2f(-size_x/2, -size_y/2)
    glVertex2f(size_x/2, -size_y/2)
    glVertex2f(size_x/2, size_y/2)
    glEnd()
    glPopMatrix()

def draw_control_bar(control_bar):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-width//2, width//2, -height//2, height//2)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPushMatrix()
    glTranslatef(control_bar.position[0], control_bar.position[1], 0)
    glTranslatef(60, 0, 0)
    glColor4f(0, 0, 0, 0.8)
    glBegin(GL_QUADS)
    glVertex2f(-control_bar.bar_limit, 3)
    glVertex2f(-control_bar.bar_limit, -3)
    glVertex2f(control_bar.bar_limit, -3)
    glVertex2f(control_bar.bar_limit, 3)
    glEnd()
    
    glTranslatef(control_bar.bar_offset, 0, 0)
    glColor4f(1, 0, 0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-7.5, 20)
    glVertex2f(-7.5, -20)
    glVertex2f(7.5, -20)
    glVertex2f(7.5, 20)
    glEnd()
    glPopMatrix()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    control_bar.text_label.draw()
    control_bar.value_label.draw()

def draw():
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_LIGHTING)
    
    draw_widget(0, -360, 1200, 200, [1, 1, 1, 0.7])
    for control_bar in control_bar_list:
        draw_control_bar(control_bar)
    
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)

def handle_mouse(x, y, dx, dy):
    for control_bar in control_bar_list:
        if abs((width//2 + control_bar.position[0] + 60 + control_bar.bar_offset) - x) < 20 and abs(height//2 + control_bar.position[1] - y) < 20:
            control_bar.bar_offset += dx
            # limit bar
            if control_bar.bar_offset > control_bar.bar_limit:
                control_bar.bar_offset = control_bar.bar_limit
            elif control_bar.bar_offset < -control_bar.bar_limit:
                control_bar.bar_offset = -control_bar.bar_limit
        
            # update value
            scale = ((control_bar.bar_offset - (-control_bar.bar_limit)) / (2 * control_bar.bar_limit))
            control_bar.value = scale * (control_bar.limit[1] - control_bar.limit[0]) + control_bar.limit[0]
            control_bar.update_text()

            break

def get_parameter(text):
    for control_bar in control_bar_list:
        if text == control_bar.text:
            return control_bar.value