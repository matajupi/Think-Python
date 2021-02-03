import math
import time

#s = time.time()
#m = s // 60
#s %= 60
#h = m // 60
#m %= 60
#d = h // 24
#h %= 24
#print(d, h, m, s)

def check_fermat(a, b, c, n):
    if n < 2:
        return
    if math.pow(a, n) + math.pow(b, n) == math.pow(c, n):
        print("Wrong")
    else:
        print("Noooo")

def is_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        print("no")
        return
    print("yes")

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    #n = int(input())
    #check_fermat(a, b, c, n)
    is_triangle(a, b, c)
