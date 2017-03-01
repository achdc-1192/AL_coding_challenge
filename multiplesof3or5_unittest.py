import unittest
from multiplesof3or5 import multiples
class TestForMultiplesof3or5(unittest.TestCase):
    def test_number(self):
        self.assertEqual(multiples(16), 60)
    def test_invalid_number(self):
        self.assertEqual(multiples("iamanurag"), "Enter a valid number!")
    def test_negative_number(self):
        self.assertEqual(multiples(-4654798),0)
if __name__ == '__main__':
    unittest.main()