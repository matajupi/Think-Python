class Test:
    num = 0

    def __init__(self):
        self.user = User(self)
        self.user.func1()
        print(self.num)
        self.plusone()
        print(self.num)
        self.user.func1()
        print(self.num)
        self.user.func2()
        print(self.num)

    def plusone(self):
        self.num += 1

class User:
    def __init__(self, test):
        self.func1 = test.plusone

    def func2(self):
        self.func1()

test = Test()
