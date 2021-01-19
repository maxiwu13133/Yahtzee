from unittest import TestCase
from yahtzee import category_checker


class TestCategoryChecker(TestCase):

    def test_category_checker_empty_score(self):
        player_score = {"1s": '', "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '',
                        "four": '', "full": '', "small": '', "large": '', "yahtzee": '',
                        "chance": ''}
        category_score = 'b'
        expected = True
        actual = category_checker(score=player_score, target_category=category_score)
        self.assertEqual(expected, actual)

    def test_category_checker_category_already_filled(self):
        player_score = {"1s": 1, "2s": 2, "3s": 3, "4s": 4, "5s": 5, "6s": 6, "three": 15,
                        "four": 20, "full": 25, "small": 30, "large": 40, "yahtzee": '',
                        "chance": ''}
        category_score = 'd'
        expected = False
        actual = category_checker(score=player_score, target_category=category_score)
        self.assertEqual(expected, actual)

    def test_category_checker_category_filled_zero(self):
        player_score = {"1s": 0, "2s": 0, "3s": 0, "4s": 0, "5s": 0, "6s": 0, "three": 0,
                        "four": 0, "full": 0, "small": 0, "large": 0, "yahtzee": 0,
                        "chance": ''}
        category_score = 'e'
        expected = False
        actual = category_checker(score=player_score, target_category=category_score)
        self.assertEqual(expected, actual)
