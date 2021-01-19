from unittest import TestCase

from yahtzee import score_calculator


class TestScoreCalculator(TestCase):

    def test_score_calculator_same_numbers_yahtzee(self):
        player_hand = [2, 2, 2, 2, 2]
        category = 'l'
        expected = 50
        actual = score_calculator(current_hand=player_hand, target_category=category)
        self.assertEqual(expected, actual)

    def test_score_calculator_same_numbers_not_yahtzee(self):
        player_hand = [2, 2, 2, 2, 2]
        category = 'b'
        expected = 10
        actual = score_calculator(current_hand=player_hand, target_category=category)
        self.assertEqual(expected, actual)

    def test_score_calculator_same_numbers_zero_point_category(self):
        player_hand = [2, 2, 2, 2, 2]
        category = 'c'
        expected = 0
        actual = score_calculator(current_hand=player_hand, target_category=category)
        self.assertEqual(expected, actual)

    def test_score_calculator_small_straight_in_large_straight_category(self):
        player_hand = [1, 1, 2, 3, 4]
        category = 'k'
        expected = 0
        actual = score_calculator(current_hand=player_hand, target_category=category)
        self.assertEqual(expected, actual)

    def test_score_calculator_large_straight_in_chance_category(self):
        player_hand = [2, 3, 4, 5, 6]
        category = 'm'
        expected = 20
        actual = score_calculator(current_hand=player_hand, target_category=category)
        self.assertEqual(expected, actual)
