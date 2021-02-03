import math

def mysqrt(a, x):
    epsilon = 1e-20
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            return x
        x = y

def test_square_root():
    print("a", "| mysqrt(a)", "| math.sqrt(a)", "| diff")
    for i in range(9):
        res1 = mysqrt(i + 1, i + 2)
        res2 = math.sqrt(i + 1)
        print(i + 1, res1, res2, abs(res1 - res2))

test_square_root()
