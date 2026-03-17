"""
两数之和模块的单元测试
"""
import unittest
from two_sum import add_two_numbers


class TestTwoSum(unittest.TestCase):
    """测试两数之和函数"""

    def test_positive_numbers(self):
        """测试正数相加"""
        self.assertEqual(add_two_numbers(3, 5), 8)
        self.assertEqual(add_two_numbers(10, 20), 30)

    def test_negative_numbers(self):
        """测试负数相加"""
        self.assertEqual(add_two_numbers(-3, -5), -8)
        self.assertEqual(add_two_numbers(-10, 5), -5)

    def test_zero(self):
        """测试包含零的情况"""
        self.assertEqual(add_two_numbers(0, 0), 0)
        self.assertEqual(add_two_numbers(5, 0), 5)
        self.assertEqual(add_two_numbers(0, 5), 5)

    def test_float_numbers(self):
        """测试浮点数相加"""
        self.assertEqual(add_two_numbers(3.5, 2.5), 6.0)
        self.assertEqual(add_two_numbers(-1.5, 2.5), 1.0)


if __name__ == "__main__":
    unittest.main()
