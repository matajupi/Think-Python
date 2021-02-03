import math

def estimate_pi():
    res = 0
    k = 0
    loop = 0
    while True:
        res += (math.factorial(4 * k) * (1103 + 26390 * k)) / (math.factorial(k) ** 4 * 396 ** (4 * k))
        print(str(res))
        if loop == 10:
            break
        loop += 1
    res *= (2 * math.sqrt(2)) / 9801
    return 1 / res

print(estimate_pi())
