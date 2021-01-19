from unittest import TestCase
from unittest.mock import patch
import io

from yahtzee import dice_reformat


class TestDiceReformat(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dice_reformat_all_same_numbers(self, mock_stdout):
        player_hand = [6, 6, 6, 6, 6]
        dice_reformat(current_hand=player_hand)
        expected = '|o   o|    |o   o|    |o   o|    |o   o|    |o   o|\n' \
                   '|o   o|    |o   o|    |o   o|    |o   o|    |o   o|\n' \
                   '|o   o|    |o   o|    |o   o|    |o   o|    |o   o|\n' \
                   '   1          2          3          4          5\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dice_reformat_all_different_numbers(self, mock_stdout):
        player_hand = [2, 3, 4, 5, 6]
        dice_reformat(current_hand=player_hand)
        expected = '|    o|    |    o|    |o   o|    |o   o|    |o   o|\n' \
                   '|     |    |  o  |    |     |    |  o  |    |o   o|\n' \
                   '|o    |    |o    |    |o   o|    |o   o|    |o   o|\n' \
                   '   1          2          3          4          5\n'
        self.assertEqual(mock_stdout.getvalue(), expected)
