import unittest
from yamlparsing.app import foobar


class TestCommonLib(unittest.TestCase):

    def test_foobar(self):
        self.assertEqual(foobar(), 1)


if __name__ == '__main__':
    unittest.main()