from unittest import TestCase
from unittest.mock import patch

from yahtzee import roll_dice


class TestRollDice(TestCase):

    @patch('random.choices', return_value=[5, 2, 3, 1, 3])
    def test_roll_dice_all_numbers_same(self, random_number_generator):
        player_hand = [4, 4, 4, 4, 4]
        die_kept = '1'
        expected = [4, 2, 3, 1, 3]
        actual = roll_dice(current_hand=player_hand, die_kept=die_kept)
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=[1, 2, 3, 4, 5])
    def test_roll_dice_roll_same_hand(self, random_number_generator):
        player_hand = [2, 2, 2, 2, 2]
        die_kept = '12345'
        expected = [2, 2, 2, 2, 2]
        actual = roll_dice(current_hand=player_hand, die_kept=die_kept)
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=[5, 5, 5, 5, 5])
    def test_roll_dice_yahtzee(self, random_number_generator):
        player_hand = [1, 2, 3, 4, 5]
        die_kept = '0'
        expected = [5, 5, 5, 5, 5]
        actual = roll_dice(current_hand=player_hand, die_kept=die_kept)
        self.assertEqual(expected, actual)
