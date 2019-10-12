import unittest
from fizzbuzz import robot


class FizzbuzzTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def test_say_2_when_2(self):
        self.assertEqual(robot(2), '2')

    def test_say_4_when_4(self):
        self.assertEqual(robot(4), '4')

    def test_say_3_when_3(self):
        self.assertEqual(robot(3), 'fizz')

    def test_say_6_when_6(self):
        self.assertEqual(robot(6), 'fizz')

    def test_say_9_when_9(self):
        self.assertEqual(robot(9), 'fizz')

    def test_say_5_when_5(self):
        self.assertEqual(robot(5), 'buzz')

    def test_say_10_when_10(self):
        self.assertEqual(robot(10), 'buzz')

    def test_say_20_when_20(self):
        self.assertEqual(robot(20), 'buzz')

    def test_say_15_when_15(self):
        self.assertEqual(robot(15), 'fizzbuzz')

    def test_say_30_when_30(self):
        self.assertEqual(robot(30), 'fizzbuzz')

    def test_say_45_when_45(self):
        self.assertEqual(robot(45), 'fizzbuzz')
