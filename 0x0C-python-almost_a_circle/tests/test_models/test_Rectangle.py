#!/usr/bin/python3

import unittest
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle




class TestRectangle(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        """"""
        Base._Base__nb_objects = 0
        self.is1 = Rectangle(10, 10)
        self.is2 = Rectangle(2, 3, 4)
        self.is3 = Rectangle(5, 6, 7, 8, 9)
        self.is4 = Rectangle(11, 12, 13, 14)

    @classmethod
    def teardownClass(self):
        pass

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_wrong_width(self):
        with self.assertRaises(TypeError):
            Rectangle("mahdi", 2)

    def test_wrong_height(self):
        with self.assertRaises(TypeError):
            Rectangle("mahdi", 2)

    def test_wrong_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "mahdi")

    def test_wrong_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "mahdi")

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.is1.id, 1)
        self.assertEqual(self.is2.id, 2)
        self.assertEqual(self.is3.id, 9)
        self.assertEqual(self.is4.id, 3)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.is1.width, 10)
        self.assertEqual(self.is2.width, 2)
        self.assertEqual(self.is3.width, 5)
        self.assertEqual(self.is4.width, 11)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.is1.height, 10)
        self.assertEqual(self.is2.height, 3)
        self.assertEqual(self.is3.height, 6)
        self.assertEqual(self.is4.height, 12)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.is1.x, 0)
        self.assertEqual(self.is2.x, 4)
        self.assertEqual(self.is3.x, 7)
        self.assertEqual(self.is4.x, 13)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.is1.y, 0)
        self.assertEqual(self.is2.y, 0)
        self.assertEqual(self.is3.y, 8)
        self.assertEqual(self.is4.y, 14)

    def test_type_error_width(self):
        """Test non-ints for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("mahdi", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 1)

    def test_type_error_height(self):
        """Test non-ints for width"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "mahdi")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, False)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {'a': 5})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3, 4])

    def test_type_error_x(self):
        """Test non-ints for width"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 'c', 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, {'a': 5}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3, 4], 5)

    def test_type_error_x(self):
        """Test non-ints for width"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 'c', 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, {'a': 5}, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3, 4], 5)

    def test_only_x(self):
        b = Rectangle(1, 2, 3)
        self.assertEqual(b.y, 0)

    def test_width_valueerror(self):
        """Test ints <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """Test ints <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """Test ints < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(2, 1, 2, -1)


if __name__ == '__main__':
    unittest.main()
