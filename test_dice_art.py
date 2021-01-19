from unittest import TestCase

from yahtzee import dice_art


class TestDiceArt(TestCase):

    def test_dice_art(self):
        dice_int = 5
        expected = ['o   o', '  o  ', 'o   o']
        actual = dice_art(dice_int)
        self.assertEqual(expected, actual)
