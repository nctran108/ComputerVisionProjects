import numpy as np
import cv2
import matplotlib.pyplot as plt
from collections import namedtuple


class Point_2D():
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def Homogeneous(self, scale = 1):
        return np.array((self.x * scale, self.y * scale, scale)).T

    def imHomogeneous(self):
        return np.array((self.x, self.y)).T

class Line_2D():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Homogeneous(self):
        return np.array([self.a, self.b, self.c]).T