import math

print("Span" * 3)

x = 3.
print(x);

s = (4 / 3) * math.pi * 5 ** 3
print(s)

price = 24.95 * 0.6
res = price * 60 + 3 + 59 * 75
print(res)

s = (6 * 60 + 52) * 60
s += (8 * 60 + 15) * 2 + (7 * 60 + 12) * 3
m = s // 60
h = m // 60
m = m % 60
s = s % 60
print(f"{h}:{m}:{s}")

