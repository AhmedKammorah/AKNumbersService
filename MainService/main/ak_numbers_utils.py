# -*- coding: utf-8 -*-
# @Author: ahmedkammorah
# @Date:   2019-05-10 22:26:07
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-05-11 13:05:50
from MainService.main.config import NUMBER_DIC


class AKNumbersUtils(object):

    def __init__(self):
        self.number_dic = NUMBER_DIC

    def translate_number(self, num):
        if num <= 20:
            return self.number_dic.get(num, "")
        digits = self._parse_dgits(num)
        d_count = len(digits)
        i = d_count - 1
        strings = []
        while(i > 0):
            d_place = (10**i)
            if d_place == 10:
                if digits[i] == 1:
                    d = d_place * digits[i] + digits[i - 1]
                    self._add_digit_string(strings, self.number_dic.get(d, ""))
                    break
                else:
                    dig = self.number_dic.get(digits[i] * d_place, "")
                    self._add_digit_string(strings, dig)
                    if digits[i - 1] != 0:
                        if dig != "":
                            strings.append("-")
                        self._add_digit_string(
                            strings, self.number_dic.get(digits[i - 1], ""))
            else:
                if digits[i] != 0:
                    self._add_digit_string(
                        strings, self.number_dic.get(digits[i], ""))
                    self._add_digit_string(
                        strings, self.number_dic.get(d_place, ""))
                    self._add_digit_string(strings, "and")
            i -= 1
        if strings[len(strings) - 1] == "and":
            strings = strings[:-1]
        out = " ".join(strings).replace(' - ', '-')
        return out

    def _parse_dgits(self, num):
        n = num
        d_count = 0
        digits = []
        while(n > 0):
            d = n % 10
            n //= 10
            d_count += 1
            digits.append(d)
        return digits

    def _add_digit_string(self, strings, dig_s):
        if dig_s != "":
            strings.append(dig_s)

        return strings

if __name__ == "__main__":
    utils = AKNumbersUtils()
    print(utils.translate_number(1252))
    print(utils.translate_number(126))
    print(utils.translate_number(111))
    print(utils.translate_number(30))
    print(utils.translate_number(100))
    print(utils.translate_number(1000))
    print(utils.translate_number(101))
