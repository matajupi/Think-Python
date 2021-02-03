def do_twice(func, param):
    func(param)
    func(param)

def do_four(func, param):
    do_twice(func, param)
    do_twice(func, param)

def print_with_hello(param):
    print(param, "hello")

do_twice(print_twice, input())
do_four(print_twice, input())
