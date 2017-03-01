import unittest
from piglatin import piglatin
class TestingForRandomInputs(unittest.TestCase):
    def test_no_alphabets(self):
        self.assertEqual(piglatin("@123$,"),"@123$,")
    def test_multiple_sentences(self):
        self.assertEqual(piglatin("With great power comes great responsibility\n I 3anurag anurag3"),
        "ithWay reatgay owerpay omescay reatgay esponsibilityray\n Iay 3nuragaay nuragaay3")
        self.assertEqual(piglatin("Alex=+, how did you do question 21?"),"lexAay=+, owhay idday ouyay oday uestionqay 21?")
    def test_middle_numbers(self):
        self.assertEqual(piglatin("I2 am2 gr00t"), "Iay2 maay2 r00tgay")
    def test_empty_string(self):
        self.assertEqual(piglatin(""), "")

if __name__ == '__main__':
    unittest.main()