import unittest

class LevelTwoTestOne(unittest.TestCase):
    def test_pass_2_1(self):
        self.assertTrue(True)

    def test_fail_2_1(self):
        self.assertTrue(False)

class LevelTwoTestTwo(unittest.TestCase):
    def test_pass_2_2(self):
        self.assertTrue(True)

    def test_fail_2_2(self):
        self.assertTrue(False)
