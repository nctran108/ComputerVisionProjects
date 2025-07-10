from src.utils import Point_2D, Line_2D
import numpy as np

def line_intersection(line1, line2):
    x_bar = np.cross(line1, line2)

    if x_bar[2] == 0:
        print("Point at Infinity ....")
        return None

    return x_bar

def get_2d_line(point1, point2):
    x_bar_1 = Point_2D(point1).Homogeneous()
    x_bar_2 = Point_2D(point2).Homogeneous()

    l = np.cross(x_bar_1, x_bar_2)

    return l


if __name__ == "__main__":
    np.random.seed(0)

    l1 = np.random.rand(3)
    l2 = np.random.rand(3)

    intersect = line_intersection(l1, l2)

    print(intersect)

    x_1 = np.random.rand(2)
    x_2 = np.random.rand(2)

    line = get_2d_line(x_1, x_2)
    print(line)