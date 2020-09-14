"""to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots"""

from math import sqrt


class Quadratic:

    @staticmethod
    def findRoot(a, b, c):
        delta = (b ** 2) - (4 * a * c)
        root1 = (-b + sqrt(delta)) / (2 * a)
        root2 = (-b - sqrt(delta)) / (2 * a)
        return root1, root2


if __name__ == "__main__":
    try:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        c = int(input("Enter value of c: "))
    except ValueError:
        print("Please enter integer value. ")
    print(f'Roots are: {Quadratic.findRoot(a, b, c)}')
