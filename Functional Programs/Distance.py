"""Program that takes two integer command-line arguments x and y and
prints the Euclidean distance from the point (x, y) to the origin (0, 0)."""
import sys
from math import sqrt


class Distance:
    @staticmethod
    def euclideanDistance(xCoor, yCoor):
        return sqrt((xCoor - 0) ** 2 + (yCoor - 0) ** 2)


if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(Distance.euclideanDistance(x, y))
