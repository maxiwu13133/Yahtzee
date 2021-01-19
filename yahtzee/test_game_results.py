from unittest import TestCase
from yahtzee import game_results


class TestGameResults(TestCase):

    def test_game_results_regular_game(self):
        score = [{"1s": 2, "2s": 4, "3s": 3, "4s": 8, "5s": 15, "6s": 12, "three": 15, "four": 22,
                  "full": 25, "small": 30, "large": 40, "yahtzee": 50, "chance": 11},
                 {"1s": 1, "2s": 0, "3s": 3, "4s": 0, "5s": 0, "6s": 6, "three": 0, "four": 23,
                  "full": 25, "small": 30, "large": 0, "yahtzee": 0, "chance": 25}]
        expected = 'Score is 237:113\nPlayer 1 wins!'
        actual = game_results(score=score)
        self.assertEqual(expected, actual)

    def test_game_results_tie_game(self):
        score = [{"1s": 0, "2s": 4, "3s": 0, "4s": 8, "5s": 5, "6s": 12, "three": 15, "four": 22,
                  "full": 25, "small": 0, "large": 40, "yahtzee": 0, "chance": 11},
                 {"1s": 0, "2s": 4, "3s": 0, "4s": 8, "5s": 5, "6s": 12, "three": 15, "four": 22,
                  "full": 25, "small": 0, "large": 40, "yahtzee": 0, "chance": 11}]
        expected = 'Score is 142:142\nTie!'
        actual = game_results(score=score)
        self.assertEqual(expected, actual)

    def test_game_results_tie_game_same_score(self):
        score = [{"1s": 0, "2s": 0, "3s": 0, "4s": 0, "5s": 0, "6s": 0, "three": 0, "four": 0,
                  "full": 0, "small": 0, "large": 0, "yahtzee": 0, "chance": 5},
                 {"1s": 0, "2s": 0, "3s": 0, "4s": 0, "5s": 0, "6s": 0, "three": 0, "four": 0,
                  "full": 0, "small": 0, "large": 0, "yahtzee": 0, "chance": 5}]
        expected = 'Score is 142:142\nTie!'
        actual = game_results(score=score)
        self.assertEqual(expected, actual)
