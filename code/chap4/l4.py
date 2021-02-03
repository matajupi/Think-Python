import turtle
import math

# saiinnsibunnkai
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# ippanka
def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

# interface sekkei
def circle(t, r):
   # circumferance = 2 * math.pi * r
   # n = int(circumferance / 3) + 3
   # length = circumferance / n
   # polygon(t, n, length)
   arc(t, r, 360)

# tonikaku sairiyouwo kokorogakeru

if __name__ == "__main__":
    bob = turtle.Turtle()
    arc(bob, 100, 180)
    circle(bob, 100)
