import unittest

class LevelOneTestOne(unittest.TestCase):
    def test_pass_1_1(self):
        self.assertTrue(True)

    def test_fail_1_1(self):
        self.assertTrue(False)

class LevelOneTestTwo(unittest.TestCase):
    def test_pass_1_2(self):
        self.assertTrue(True)

    def test_fail_1_2(self):
        self.assertTrue(False)
