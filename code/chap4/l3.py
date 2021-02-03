import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    k = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(k)

def circle(t, r):
    length = (r * 2 * math.pi) / 100
    for i in range(100):
        t.fd(length)
        t.lt(3.6)

def arc(t, r, angle):
    length = (r * 2 * math.pi) / 100
    for i in range(int(angle / 3.6)):
        t.fd(length)
        t.lt(3.6)

bob = turtle.Turtle()
# print(bob)
# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)

square(bob, 100)
polygon(bob, 100, 5)
circle(bob, 100)
bob.fd(100)
arc(bob, 100, 90)
turtle.mainloop()
