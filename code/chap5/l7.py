def countdown(n):
    if n <= 0:
        print("Blastoff")
        return
    print(n)
    countdown(n - 1)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print()
    print("print_n")
    print("s ->", s)
    print("n ->", n)
    print_n(s, n - 1)

def do_n(func, n):
    if n <= 0:
        return
    func()
    do_n(func, n - 1)

if __name__ == "__main__":
   # countdown(3)
   # s = "Hello"
   # n = 6
   # print("<module>")
   # print("s ->", s)
   # print("n ->", n)
   # print()
   # print_n(s, n)
   do_n(lambda: print("Hello Security world"), 6)
