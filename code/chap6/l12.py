def b(z):
    print("b")
    print("z ->", z)
    print()
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    print("a")
    print("x ->", x)
    print("y ->", y)
    print()
    return x * y

def c(x, y, z):
    total = x + y + z
    print("c")
    print("x ->", x)
    print("y ->", y)
    print("z ->", z)
    print("total ->", total)
    print()
    square = b(total) ** 2
    return square

def ackermann(m, n):
    print("ackermann")
    print("m ->", m)
    print("n ->", n)
    print()
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))

#x = 1
#y = x + 1
#print("module")
#print("x ->", x)
#print("y ->", y)
#print()
#print(c(x, y + 3, x + y))

print(ackermann(3, 4))
