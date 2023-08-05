import unittest
from commonlib.functions import sum_func


class TestCommonLib(unittest.TestCase):

    def test_sum(self):
        self.assertTrue(sum_func(1, 2), 3)


if __name__ == '__main__':
    unittest.main()