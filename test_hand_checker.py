from unittest import TestCase

from yahtzee import hand_checker


class TestHandChecker(TestCase):

    def test_hand_checker_yahtzee(self):
        hand = [6, 6, 6, 6, 6]
        target_category = 'l'
        expected = True
        actual = hand_checker(hand, target_category)
        self.assertEqual(expected, actual)

    def test_hand_checker_yahtzee_not_valid(self):
        hand = [2, 3, 4, 3, 4]
        target_category = 'l'
        expected = False
        actual = hand_checker(hand, target_category)
        self.assertEqual(expected, actual)
