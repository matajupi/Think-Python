import turtle
import math

 
def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)
    
def draw_triangle(t, centerangle, length):
    """Draws a triangle.

    t: Turtle
    centerangle: center angle of triangle
    length: length of center line
    """
    subangle = (180 - centerangle) / 2
    t.fd(length)
    t.lt(subangle)
    

def draw_pi(t, n, length):
    """Draws a pi.
    
    t: Turtle
    n: number of sides
    length: length of center line
    """
    centerangle = 360 / n


if __name__ == "__main__":
    t = turtle.Turtle()
    turtle.mainloop()
