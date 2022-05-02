import math
from geom2d import nums

class Vector:
    def __init__(self, u, v):
        self.u = u
        self.v = v

    def __add__(self, other):
        return Vector(
            self.u + other.u,
            self.v + other.v
        )

    def __sub__(self, other):
        return Vector(
            self.u - other.u,
            self.v - other.v
        )

    def scaled_by(self, factor):
        return Vector(factor * self.u, factor * self.v)


    @property
    def norm(self):
        return math.sqrt(self.u ** 2 + self.v ** 2)

    @property
    def is_normal(self):
        return nums.is_close_to_one(self.norm)

    def normalized(self):
        return self.scaled_by(1.0 / self.norm)

    def with_length(self, length):
        return self.normalized().scaled_by(length)

    def dot(self, other):
        return (self.u * other.u) + (self.v * other.v)

    def projection_over(self, direction):
        return self.dot(direction.normalized())

    def cross(self, other):
        return (self.u * other.v) - (self.v * other.u)

    def is_parallel_to(self, other):
        return nums.is_close_to_zero(self.cross(other))

    def is_perpendicular_to(self, other):
        return nums.is_close_to_zero(self.dot(other))
