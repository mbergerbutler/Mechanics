import unittest
import math

from geom2d.circle import Circle
from geom2d.point import Point

class TestCircle(unittest.TestCase):
    point = Point(0, 0)
    radius = 1.0
    circle = Circle(point, radius)

    p1 = Point(0.5, 0)
    p2 = Point(2, 0)

    def test_area(self):
        expected = math.pi
        actual = self.circle.area
        self.assertAlmostEqual(expected, actual)

    def test_circumference(self):
        expected = 2 * math.pi
        actual = self.circle.circumference
        self.assertAlmostEqual(expected, actual)

    def test_contains_point(self):
        self.assertTrue(self.circle.contains_point(self.p1))

    def test_doesnt_contain_point(self):
        self.assertFalse(self.circle.contains_point(self.p2))