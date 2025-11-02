import serial
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

PORT = "COM6"
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)

vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

edges = [
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4),
    (0,4), (1,5), (2,6), (3,7)
]

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    x_angle = 0
    y_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ser.close()
                pygame.quit()
                return

        try:
            data = ser.readline().decode('utf-8').strip()
            if data:
                x, y, button = data.split(',')
                x = int(x)
                y = int(y)
                button = int(button)

                x_angle += x * 0.01
                y_angle += y * 0.01

                if button == 0:
                    glTranslatef(0, 0, 0.2)
                else:
                    glTranslatef(0, 0, -0.05)

        except Exception:
            pass

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(x_angle, 1, 0, 0)
        glRotatef(y_angle, 0, 1, 0)
        Cube()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
