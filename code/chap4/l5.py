import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def draw_petal(t, r, angle):
    """ Draw pental.
    t: Turtle
    r: radius of petal
    angle: angle of pental curve """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def draw_flower(t, pnum, pr, pangle):
    """Draw flower.
    t: Turtle
    pnum: number of petals
    pr: radius of petals
    pangle: angle of petals curve"""
    if pangle > 180:
        raise Exception()
    n = 360 / pnum
    for i in range(pnum):
        draw_petal(t, pr, pangle)
        t.lt(n)

if __name__ == "__main__":
    t = turtle.Turtle()
    pnum = int(input("pnum: "))
    pr = int(input("pradius: "))
    pangle = int(input("pangle: "))
    draw_flower(t, pnum, pr, pangle)
    turtle.mainloop()
