from math import *

class MathBase:

    x = 0
    y = 0
    z = 0

    def set(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c

    def show(self):
        print('x =', self.x, '\n', 'y =', self.y, '\n', 'z =', self.z, '\n')

    def solution(self):
        u = ((8 + abs(self.x - self.y) ** 2 + 1) ** (1 / 3) / (self.x ** 2 + self.y ** 2 + 2)) - exp(abs(self.x - self.y)) * (tan(self.z) ** 2 + 1) ** self.x
        print('Value of u ', u)


objU = MathBase()
objU.set(-4.5, 0.75*(10**(-4)), 0.845*10**2)
objU.show()
objU.solution()