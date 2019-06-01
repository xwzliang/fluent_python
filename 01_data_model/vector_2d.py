from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __repr__ specify the string representation of the object, so now vector instances are shown in the console like Vector(1, 2) instead of "<Vecor object at 0x10e100070>"
    def __repr__(self):
        # The %s specifier converts the object using str(), and %r converts it using repr(), so ues %r gives us Vector(1, 2) instead of Vector('1', '2')
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
