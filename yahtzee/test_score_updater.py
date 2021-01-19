from unittest import TestCase
from yahtzee import score_updater


class TestScoreUpdater(TestCase):

    def test_score_updater_large_straight(self):
        score = {"1s": '', "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '',
                 "four": '', "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''}
        hand = [1, 2, 3, 4, 5]
        category = 'k'
        expected = {"1s": '', "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '',
                    "four": '', "full": '', "small": '', "large": 40, "yahtzee": '', "chance": ''}
        actual = score_updater(score=score, current_hand=hand, target_category=category)
        self.assertEqual(expected, actual)

    def test_score_updater_yahtzee(self):
        score = {"1s": 1, "2s": 2, "3s": 3, "4s": 4, "5s": 5, "6s": 6, "three": '', "four": '',
                 "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''}
        hand = [3, 3, 3, 3, 3]
        category = 'l'
        expected = {"1s": 1, "2s": 2, "3s": 3, "4s": 4, "5s": 5, "6s": 6, "three": '', "four": '',
                    "full": '', "small": '', "large": '', "yahtzee": 50, "chance": ''}
        actual = score_updater(score=score, current_hand=hand, target_category=category)
        self.assertEqual(expected, actual)

    def test_score_updater_second_yahtzee(self):
        score = {"1s": 1, "2s": 2, "3s": 3, "4s": 4, "5s": 5, "6s": 6, "three": '', "four": '',
                 "full": '', "small": '', "large": '', "yahtzee": 50, "chance": ''}
        hand = [5, 5, 5, 5, 5]
        category = 'l'
        expected = {"1s": 1, "2s": 2, "3s": 3, "4s": 4, "5s": 5, "6s": 6, "three": '', "four": '',
                    "full": '', "small": '', "large": '', "yahtzee": 150, "chance": ''}
        actual = score_updater(score=score, current_hand=hand, target_category=category)
        self.assertEqual(expected, actual)

    def test_score_updater_upper_section_bonus(self):
        score = {"1s": 3, "2s": 6, "3s": 9, "4s": '', "5s": 15, "6s": 18, "three": 0, "four": '',
                 "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''}
        hand = [4, 4, 4, 1, 2]
        category = 'd'
        expected = {"1s": 3, "2s": 6, "3s": 9, "4s": 12, "5s": 15, "6s": 18, "three": 0, "four": '',
                    "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''}
        actual = score_updater(score=score, current_hand=hand, target_category=category)
        self.assertEqual(expected, actual)
