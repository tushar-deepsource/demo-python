"""Doc"""
import unittest
from demo_code import f


class Tests(unittest.TestCase):
    """Doc"""

    def my_test(self):
        """Doc"""
        self.assertEquals(f(), None)
