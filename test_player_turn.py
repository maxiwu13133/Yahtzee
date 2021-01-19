from unittest import TestCase

from yahtzee import player_turn


class TestPlayerTurn(TestCase):

    def test_player_turn_first_round(self):
        score = {0: {"1s": 1, "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '',
                 "four": '', "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''},
                 1: {"1s": '', "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '',
                 "four": '', "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''}}
        player = 1
        expected = 0
        actual = player_turn(score, player)
        self.assertEqual(expected, actual)

    def test_player_turn_last_round(self):
        score = {0: {"1s": 2, "2s": 4, "3s": 3, "4s": 8, "5s": 15, "6s": 12, "three": 15,
                     "four": 22, "full": 25, "small": 30, "large": 40, "yahtzee": 50, "chance": 11},
                 1: {"1s": 0, "2s": 4, "3s": 0, "4s": 8, "5s": 5, "6s": 12, "three": 15,
                     "four": 9, "full": 25,"small": 0, "large": 40, "yahtzee": 0, "chance": 11}}
        player = 0
        expected = 2
        actual = player_turn(score, player)
        self.assertEqual(expected, actual)
