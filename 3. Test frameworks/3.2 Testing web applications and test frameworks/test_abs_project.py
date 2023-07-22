import pytest
import unittest

# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of number"
#
# if __name__ == '__main__':
#     test_abs1()
#     print('All test passed')


# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("Everything passed")

class TestAbs(unittest.TestCase):

    def test_abs1(self):
        self.assertEqual(abs(-42) == 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42) == -42, "Should be absolute value of a number")

if __name__ == 'main':
    unittest.main()
