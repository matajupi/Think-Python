def recurse(n, s):
    """n: 0 < n"""
    print("recurse")
    print("n ->", n)
    print("s ->", s)
    print()
    if n == 0:
        print(s)
        return
    recurse(n - 1, n + s)

if __name__ == "__main__":
    recurse(3, 0)
    recurse(-1, 0)
