from math import *


class X:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Y:
    def __init__(self, z):
        self.z = z


objX = X(-4.5, 0.75*10**(-4))
objY = Y(0.845*10**2)


def show(X, Y):
    print(' x = ', X.x,'\n', 'y = ', X.y,'\n', 'z = ', Y.z,'\n')


show(objX, objY)


def solution(X, Y):
    print(((8 + abs(X.x - X.y) ** 2 + 1) ** (1 / 3) / (X.x ** 2 + X.y ** 2 + 2)) - exp(abs(X.x - X.y)) * (tan(Y.z) ** 2 + 1) ** X.x)


solution(objX, objY)
