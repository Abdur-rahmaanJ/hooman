cube

![](https://github.com/Abdur-rahmaanJ/hooman/raw/master/assets/cube.gif)

```python
"""
Thanks to Kostas Terzidis

Abdur-Rahmaan Janhangeer
https://github.com/Abdur-RahmaanJ
"""

from hooman import Hooman
from math import *

window_width, window_height = 500, 500
hapi = Hooman(window_width, window_height)


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def move(self, xoff, yoff, zoff):
        self.x = self.x + xoff
        self.y = self.y + yoff
        self.z = self.z + zoff

    def scale(self, xoff, yoff, zoff):
        self.x = self.x * xoff
        self.y = self.y * yoff
        self.z = self.z * zoff

    def rotatez(self, angle):
        tempx = self.x * cos(angle) - self.y * sin(angle)
        tempy = self.y * cos(angle) + self.x * sin(angle)
        self.x = tempx
        self.y = tempy

    def rotatex(self, angle):
        tempy = self.y * cos(angle) - self.z * sin(angle)
        tempz = self.z * cos(angle) + self.y * sin(angle)
        self.y = tempy
        self.z = tempz

    def rotatey(self, angle):
        tempx = self.x * cos(angle) - self.z * sin(angle)
        tempz = self.z * cos(angle) + self.x * sin(angle)
        self.x = tempx
        self.z = tempz

    def xP(self, eye):
        t = 1.0 / (1.0 + (self.z / eye))
        px = int(self.x * t)
        return px

    def yP(self, eye):
        t = 1.0 / (1.0 + (self.z / eye))
        py = int(self.y * t)
        return py


points = [
    Point(-50, -50, -50),
    Point(50, -50, -50),
    Point(50, 50, -50),
    Point(-50, 50, -50),
    Point(-50, -50, 50),
    Point(50, -50, 50),
    Point(50, 50, 50),
    Point(-50, 50, 50),
]


dragging = False


offset_x = hapi.WIDTH // 2
offset_y = hapi.HEIGHT // 2

while hapi.is_running:
    bg_col = (255, 255, 255)
    hapi.background(bg_col)
    hapi.fill(0)

    try:
        hapi.stroke_size(3)
        hapi.stroke(0)
        for p1 in points:
            for p2 in points:
                hapi.line(
                    offset_x + p1.x, offset_y + p1.y, offset_x + p2.x, offset_y + p2.y
                )
                # mouse_coords = (hapi.mouseX(), hapi.mouseY())
                # eye = hapi.dist((0, 0), mouse_coords)
                # if eye <= 0:
                #     eye = 1
                # hapi.line(50+p1.xP(eye), 50+ p1.yP(eye), 50+p2.xP(eye), 50+p2.yP(eye) )

    except Exception as e:
        raise
    else:
        pass
    finally:
        pass

    # for i in range(8):
    #     hapi.ellipse( 50+ points[i].x, 50+ points[i].y, 5, 5)

    pmouseX = hapi.mouseX()
    pmouseY = hapi.mouseY()

    for event in hapi.pygame.event.get():

        if event.type == hapi.pygame.KEYDOWN:
            pass

        elif event.type == hapi.pygame.MOUSEBUTTONDOWN:

            dragging = True
            break

        elif event.type == hapi.pygame.MOUSEBUTTONUP:
            draging = False

        elif event.type == hapi.pygame.MOUSEMOTION:
            if dragging:

                xoff = hapi.mouseX() - pmouseX
                yoff = hapi.mouseY() - pmouseY

                for i, point in enumerate(points):
                    point.rotatey(radians(xoff))
                    point.rotatex(radians(yoff))

    hapi.fill((255, 0, 0))

    hapi.ellipse(hapi.mouseX(), hapi.mouseY(), 5, 5)

    hapi.flip_display()
    hapi.event_loop()

hapi.pygame.quit()
```