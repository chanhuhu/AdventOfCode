import itertools
import unittest

def openfile(filename: str):

    with open(filename, 'r') as f:
        entries = []
        for i in f.read().split("\n"):
            if i:
                entries.append(int(i))

    return entries

def day1a(filename: str):
    file = openfile(filename=filename)

    for a,b in itertools.permutations(file, 2):
        target: int = 2020 - a
        if target == b:
            return a * b

    return -1

def day1b(filename: str) -> int:
    file = openfile(filename=filename)

    for a,b,c in itertools.permutations(file, 3):

        if a + b + c == 2020:
            return a * b * c

    return -1

class Test(unittest.TestCase):

    def test_day1a_example(self):
        file = 'a.input.example.txt'
        result = 514579
        self.assertEqual(result, day1a(file))

    def test_day1a(self):
        file = 'a.input.txt'
        result = 1020099
        self.assertEqual(result, day1a(file))

    def test_day1b(self):
        file = 'b.input.txt'
        result = 1020099
        print(day1b(file))
        self.assertEqual(result, day1a(file))

if __name__ == '__main__':
    unittest.main()
