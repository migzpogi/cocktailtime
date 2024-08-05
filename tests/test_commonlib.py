import unittest
from commonlib.functions import sum_func, is_datestring_iso8600


class TestCommonLib(unittest.TestCase):

    def test_sum(self):
        self.assertTrue(sum_func(1, 2), 3)

    def test_datestring(self):
        self.assertTrue(sum_func(1, 2), 3)


if __name__ == '__main__':
    unittest.main()