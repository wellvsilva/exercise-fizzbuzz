"""
Regras do Fizzbuzz

1. Se a posição for múltipla de 3: fizz
2. Se a posição for múltipla de 5: buzz
3. Se a posição for múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio número

"""
from functools import partial
import unittest


multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(pos):
    say = str(pos)

    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'

    elif multiple_of_5(pos):
        say = 'buzz'

    elif multiple_of_3(pos):
        say = 'fizz'

    return say


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

if __name__ == '__main__':
    unittest.main()
