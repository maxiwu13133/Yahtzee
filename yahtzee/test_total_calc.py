from unittest import TestCase

from yahtzee import total_calc


class TestTotalCalc(TestCase):

    def test_total_calc_no_scores(self):
        score = {"1s": '', "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '',
                 "four": '', "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''}
        expected = 0
        actual = total_calc(score)
        self.assertEqual(expected, actual)

    def test_total_calc_perfect_score(self):
        score = {"1s": 5, "2s": 10, "3s": 15, "4s": 20, "5s": 25, "6s": 30, "three": 30,
                 "four": 30, "full": 25, "small": 30, "large": 40, "yahtzee": 50, "chance": 30}
        expected = 480
        actual = total_calc(score)
        self.assertEqual(expected, actual)
