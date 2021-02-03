import math
# print(eval('type(math.pi)'))
# print(eval('1 + 2 * 3'))

def eval_loop():
    res = None
    while True:
        query = input()
        if query == "done":
            return res
        try:
            res = eval(query)
            print(res)
        except:
            print("Notfound")

print(eval_loop())
