import unittest
from chroniker.main import logic


class TestMain(unittest.TestCase):
    def test_logic(self):
        self.assertEqual("Hello World!", logic())
