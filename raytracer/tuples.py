import math

EPSILON = 0.00001


def equal(a, b):
    if abs(a - b) < EPSILON:
        return True
    else:
        return False


class Tuple:
    def __init__(self, x, y, z, w):
        self._x = x
        self._y = y
        self._z = z
        self._w = w

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def w(self):
        return self._w

    def __eq__(self, other):
        if isinstance(self, Tuple):
            return (
                equal(self.x, other.x) and
                equal(self.y, other.y) and
                equal(self.z, other.z) and
                equal(self.w, other.w)
            )
        else:
            return False

    def __add__(self, other):
        return self.__class__(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w
        )

    def __sub__(self, other):
        return self.__class__(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w
        )

    def __neg__(self):
        return self.__class__(
            -self.x,
            -self.y,
            -self.z,
            -self.w
        )

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(
                self.x * other,
                self.y * other,
                self.z * other,
                self.w * other
            )
        else:
            raise TypeError('Can only perform scalar multiply with int or float')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(
                self.x / other,
                self.y / other,
                self.z / other,
                self.w / other
            )
        else:
            raise TypeError('Can only perform scalar division with int or float')

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)

    def normalize(self):
        length = self.magnitude()
        if length:
            return self.__class__(
                self.x / length,
                self.y / length,
                self.z / length,
                self.w / length
            )
        else:
            return self.__class__(0, 0, 0, 0)


class Point(Tuple):
    def __init__(self, x, y, z, w=1.0):
        super().__init__(x, y, z, w)


class Vector(Tuple):
    def __init__(self, x, y, z, w=0.0):
        super().__init__(x, y, z, w)
