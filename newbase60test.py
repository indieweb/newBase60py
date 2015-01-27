'''unit tests for newbase60.py '''

import newbase60
import unittest

class SpotCheckToBase60(unittest.TestCase):
    def test_check0(self):
        self.assertEqual(newbase60.numtosxg(0), '0')
    def test_check1(self):
        self.assertEqual(newbase60.numtosxg(1), '1')
    def test_check60(self):
        self.assertEqual(newbase60.numtosxg(60), '10')

class SpotCheckFromBase60(unittest.TestCase):
    def test_check0(self):
        self.assertEqual(newbase60.sxgtonum('0'), 0)
    def test_check1(self):
        self.assertEqual(newbase60.sxgtonum('1'), 1)
    def test_check60(self):
        self.assertEqual(newbase60.sxgtonum('10'), 60)
    def test_check1337(self):
        self.assertEqual(newbase60.sxgtonum('NH'), 1337)
    def test_checkl(self):
        self.assertEqual(newbase60.sxgtonum('l'), 1)
    def test_checkI(self):
        self.assertEqual(newbase60.sxgtonum('I'), 1)
    def test_checkO(self):
        self.assertEqual(newbase60.sxgtonum('O'), 0)
    def test_checkpipe(self):
        self.assertEqual(newbase60.sxgtonum('|'), 0)
    def test_checkcomma(self):
        self.assertEqual(newbase60.sxgtonum(','), 0)

class RoundtripCheck(unittest.TestCase):
    def test_roundtrip(self):
        '''sxgtonum(numtosxg(n))==n for all n'''
        for integer in range(0, 6000):
            sxg = newbase60.numtosxg(integer)
            result = newbase60.sxgtonum(sxg)
            self.assertEqual(integer, result)

if __name__ == '__main__':
    unittest.main()
