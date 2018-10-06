class X:
    x1 = 0
    x2 = 0

    def __init__(self, a, b):
        self.x1 = a
        self.x2 = b

    def changeX(self, a, b):
        self.x1 = a
        self.x2 = b

class Y(X):
    y1 = 0

    def set(self, y):
        self.y1 = y

    def out(self):
        print(self.x1, self.x2, self.y1)

    def solution(self):
        self.answer = self.x1 * self.x2 * self.y1
        print(self.answer)


obj = Y(2, 4)
obj.set(8)
obj.out()
obj.solution()



