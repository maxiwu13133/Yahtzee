from unittest import TestCase

from yahtzee import upper_calc


class TestUpperCalc(TestCase):

    def test_upper_calc_no_upper_bonus(self):
        score = {"1s": 2, "2s": 4, "3s": 3, "4s": 8, "5s": 15, "6s": 12, "three": 15, "four": 22,
                 "full": 25, "small": 30, "large": 40, "yahtzee": 50, "chance": 11}
        expected = 0
        actual = upper_calc(score)
        self.assertEqual(expected, actual)

    def test_upper_calc_exactly_sixty_three(self):
        score = {"1s": 3, "2s": 6, "3s": 9, "4s": 12, "5s": 15, "6s": 18, "three": 15, "four": 22,
                 "full": 25, "small": 30, "large": 40, "yahtzee": '', "chance": 11}
        expected = 98
        actual = upper_calc(score)
        self.assertEqual(expected, actual)

    def test_upper_calc_highest_score(self):
        score = {"1s": 5, "2s": 10, "3s": 15, "4s": 20, "5s": 25, "6s": 30, "three": 15, "four": 22,
                 "full": 25, "small": 30, "large": '', "yahtzee": '', "chance": 11}
        expected = 140
        actual = upper_calc(score)
        self.assertEqual(expected, actual)