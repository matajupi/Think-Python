import math

def area(radius):
    a = math.pi * radius ** 2
    return a

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

def hikaku(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    #print("dx is", dx)
    #print("dy is", dy)
    #print("dsquared is", dsquared)
    result = math.sqrt(dsquared)
    return result

def hypotenuse(h1, h2):
    return math.sqrt(h1 ** 2 + h2 ** 2)

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    return area(radius)

def is_divisible(x, y):
    return x % y == 0

def factorial(n):
    if not isinstance(n, int):
        print("Error")
        return None
    elif n < 0:
        print("Error")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    # print(hikaku(1, 2))
    # print(hikaku(2, 1))
    # print(hikaku(2, 2))
    #print(distance(1, 2, 4, 6))
    #print(hypotenuse(3, 4))
    #print(circle_area(1, 3, 7, 4))
    #print(is_divisible(6, 4))
    #print(factorial(3))
    print(factorial(-1))
    print(factorial(3))
    for i in range(10):
        print(fibonacci(i))
