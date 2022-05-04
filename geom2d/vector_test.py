import unittest
import math
from geom2d.vector import Vector

class TestVector(unittest.TestCase):
    u = Vector(1, 2)
    v = Vector(4, 6)
    n = Vector(0, 1)
    k = Vector(0, 2)

    def test_plus(self):
        expected = Vector(5, 8)
        actual = self.u + self.v
        self.assertEqual(expected, actual)

    def test_minus(self):
        expected = Vector(-3, -4)
        actual = self.u - self.v
        self.assertEqual(expected, actual)

    def test_dot_product(self):
        expected = 16
        actual = self.u.dot(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_cross_product(self):
        expected = -2
        actual = self.u.cross(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_are_parallel(self):
        self.assertTrue(self.u.is_parallel_to(self.u))

    def test_are_not_parallel(self):
        self.assertFalse(self.u.is_parallel_to(self.v))

    def test_are_perpendicular(self):
        perp = Vector(-2, 1)
        self.assertTrue(self.u.is_perpendicular_to(perp))

    def test_are_not_perpendicular(self):
        self.assertFalse(self.u.is_perpendicular_to(self.v))

    def test_scaled_by(self):
        expected = Vector(2, 4)
        actual = self.u.scaled_by(2)
        self.assertEqual(expected, actual)

    def test_norm(self):
        expected = math.sqrt(1 ** 2 + 2 ** 2)
        actual = self.u.norm
        self.assertAlmostEqual(expected, actual)

    def test_is_normal(self):
        self.assertTrue(self.n.is_normal)

    def test_is_not_normal(self):
        self.assertFalse(self.u.is_normal)

    def test_normalized(self):
        expected = Vector(0, 1)
        actual = self.k.normalized()
        self.assertEqual(expected, actual)

    def test_with_length(self):
        expected = Vector(0, 2)
        actual = self.n.with_length(2)
        self.assertEqual(expected, actual)

    def test_projection_over(self):
        expected = 2.0
        actual = self.u.projection_over(self.n)
        self.assertAlmostEqual(expected, actual)

