def is_power(a, b):
    if a == b:
        return True
    if a % b:
        return False
    a /= b
    return is_power(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

#print(is_power(int(input()), int(input())))
print(gcd(int(input()), int(input())))
