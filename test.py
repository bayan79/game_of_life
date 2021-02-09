import unittest
from rule_30 import gen


class TestGen(unittest.TestCase):
    def test_gen(self):
        g = gen()
        n = int(input('skip n iter\n'))
        for _ in range(n):
            next(g)
        output = [next(g) for _ in range(20)]
        self.assertEqual(output,
                         [1, 1, 0, 0, 1, 1, 1, 1, 0, 0,
                          1, 1, 1, 1, 1, 1, 0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
