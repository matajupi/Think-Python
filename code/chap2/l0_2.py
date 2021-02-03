message = "What am I doing. This is too easy!"
pi = 3.1415926535897932384
s = 2 ** 2 * pi
print(s)
print(message + " Hoge")

import math

print(5 ** 3 * math.pi * (4 / 3))
print(60 * (24.95 * 0.6) + 3 + 59 * 0.75)
s = 52 * 60
s += 8 * 60 + 15
s += 3 * (7 * 60 + 12)
s += 8 * 60 + 15
m = s // 60
h = m // 60
m = m % 60
print(6 + h, ":", m)
