import math

#print(math.log10(3))
#print(math.sin(math.pi / 2))

# degrees = 45
# radians = degrees / 360.0 * 2 * math.pi
# print(math.sin(radians))
# print(math.sqrt(2) / 2)

#def right_justify(sentens):
#    l = len(sentens)
#    if l > 70:
#        del l[70:]
#        return l
#    while len(sentens) < 70:
#        sentens = "a" + sentens
#    return sentens
#
#if __name__ == "__main__":
#    sentens = input()
#    print(right_justify(sentens))

#def do_some(f, arg, loop=2):
#    for i in range(loop):
#        f(arg)
#
#def print_twice(arg):
#    print(arg)
#    print(arg)
#
#do_some(print_twice, 'spam', 2)

def print_sq(width, height):
    p1 = "+" + "".join("-" for i in range(width)) + "+" + "".join("-" for i in range(width)) + "+"
    p2 = "|" + "".join(" " for i in range(width)) + "|" + "".join(" " for i in range(width)) + "|"
    for i in range(2):
        print(p1)
        for i in range(height):
            print(p2)    
    print(p1)

width = int(input())
height = int(input())
print_sq(width, height)
