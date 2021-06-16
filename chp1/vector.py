class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(scalar * self.x, scalar * self.y)

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y





v1 = Vector(3, 4)
v2 = Vector(4, 5)

v1

v2

v1 + v2

v1 * 3

v1 @ v2


