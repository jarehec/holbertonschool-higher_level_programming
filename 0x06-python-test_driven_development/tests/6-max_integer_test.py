#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        test = [3, 53, 70]
        result = max_integer(test)
        self.assertEqual(result, 70)

    def test_neg_max_integer(self):
        test = [-43, 53, -70]
        result = max_integer(test)
        self.assertEqual(result, 53)

    def test_neg_integer(self):
        test = [-43]
        result = max_integer(test)
        self.assertEqual(result, -43)

    def test_max_integer(self):
        test = ([99999999999999999999999, 1])
        result = max_integer(test)
        self.assertEqual(result, 99999999999999999999999)

    def test_max_integer_end(self):
        test = ([1, 99999999999999999999999])
        result = max_integer(test)
        self.assertEqual(result, 99999999999999999999999)

    def test_max_integer_tup(self):
        test = max_integer([(1, 1), (99, 99)])
        result = max_integer(test)
        self.assertEqual(result, 99)

    def test_str_in_test(self):
        test = ['hi', 53, -70]
        with self.assertRaises(TypeError):
            result = max_integer(test)

    def test_empty(self):
        test = ()
        result = max_integer(test)
        self.assertEqual(result, None)

    def test_empty_list(self):
        test = ([])
        result = max_integer(test)
        self.assertEqual(result, None)

    def test_boolean(self):
        test = [True, -43, 0]
        result = max_integer(test)
        self.assertEqual(result, True)

    def test_None(self):
        test = [None, None]
        with self.assertRaises(TypeError):
            result = max_integer(test)

    def test_too(self):
        test = [None, None]
        with self.assertRaises(TypeError):
            result = max_integer(test)

if __name__ == '__main__':
    unittest.main()
