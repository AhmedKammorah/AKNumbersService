# -*- coding: utf-8 -*-
# @Author: Ahmed kammorah
# @Date:   2019-05-10 23:13:06
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-05-11 13:07:09
import unittest

from MainService.main.ak_numbers_utils import AKNumbersUtils
class TestAKNumbersUtils(unittest.TestCase):

    def setUP(self):
        pass

    def test_translate_number(self):
        self.util = AKNumbersUtils()
        self.assertEqual(self.util.translate_number(1), "one")
        self.assertEqual(self.util.translate_number(8), "eight")
        self.assertEqual(self.util.translate_number(10), "ten")
        self.assertEqual(self.util.translate_number(19), "nineteen")
        self.assertEqual(self.util.translate_number(21), "twenty-one")
        self.assertEqual(self.util.translate_number(35), "thirty-five")
        self.assertEqual(self.util.translate_number(111), "one hundred and eleven")
        self.assertEqual(self.util.translate_number(119), "one hundred and nineteen")
        self.assertEqual(self.util.translate_number(247), "two hundred and forty-seven")
        self.assertEqual(self.util.translate_number(512), "five hundred and twelve")
        self.assertEqual(self.util.translate_number(748), "seven hundred and forty-eight")
        self.assertEqual(self.util.translate_number(999), "nine hundred and ninety-nine")

        self.assertEqual(self.util.translate_number(20), "twenty")
        self.assertEqual(self.util.translate_number(30), "thirty")
        self.assertEqual(self.util.translate_number(70), "seventy")
        self.assertEqual(self.util.translate_number(100), "one hundred")
        self.assertEqual(self.util.translate_number(200), "two hundred")

        self.assertEqual(self.util.translate_number(101), "one hundred and one")
        self.assertEqual(self.util.translate_number(503), "five hundred and three")
        self.assertEqual(self.util.translate_number(650), "six hundred and fifty")
        
        



if __name__ == "__main__":
    unittest.main()