import turtle

def koch(t, x):
    if x < 3:
        t.fd(x)
        return
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)
    t.rt(120)
    koch(t, x / 3)
    t.lt(60)
    koch(t, x / 3)


if __name__ == "__main__":
    t = turtle.Turtle()
    t.penup()
    t.goto(-750, -300)
    t.pendown()
    koch(t, 1000)
    turtle.mainloop()

