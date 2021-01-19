from unittest import TestCase
from yahtzee import display_scoreboard


class TestDisplayScoreboard(TestCase):

    def test_display_scoreboard_filled_scoreboard(self):
        score = {"1s": 2, "2s": 4, "3s": 3, "4s": 8, "5s": 15, "6s": 12, "three": 15, "four": 22,
                 "full": 25, "small": 30, "large": 40, "yahtzee": 50, "chance": 11}
        expected = "[a)     1's       ]  2	   [g)Three of a kind]  15\n" \
                   "[b)     2's       ]  4	   [h) four of a kind]  22\n" \
                   "[c)     3's       ]  3	   [i)   full house  ]  25\n" \
                   "[d)     4's       ]  8	   [j) small straight]  30             [total]  237\n" \
                   "[e)     5's       ]  15    [k) large straight]  40\n" \
                   "[f)     6's       ]  12	   [l)    yahtzee    ]  50\n" \
                   "[   upper bonus   ]  0     [m)    chance     ]  11"
        actual = display_scoreboard(score=score)
        self.assertEqual(expected, actual)

    def test_display_scoreboard_empty_scoreboard(self):
        score = {"1s": '', "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '',
                 "four": '', "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''}
        expected = "[a)     1's       ]   	   [g)Three of a kind]    \n" \
                   "[b)     2's       ]  	   [h) four of a kind]    \n" \
                   "[c)     3's       ]  	   [i)   full house  ]    \n" \
                   "[d)     4's       ]  	   [j) small straight]                 [total]  0\n" \
                   "[e)     5's       ]        [k) large straight]    \n" \
                   "[f)     6's       ]  	   [l)    yahtzee    ]    \n" \
                   "[   upper bonus   ]        [m)    chance     ]      "
        actual = display_scoreboard(score=score)
        self.assertEqual(expected, actual)

    def test_display_scoreboard_lowest_score(self):
        score = {"1s": 0, "2s": 0, "3s": 0, "4s": 0, "5s": 0, "6s": 0, "three": 0, "four": 0,
                 "full": 0, "small": 0, "large": 0, "yahtzee": 0, "chance": 5}
        expected = "[a)     1's       ]  0	   [g)Three of a kind]  0  \n" \
                   "[b)     2's       ]  0	   [h) four of a kind]  0  \n" \
                   "[c)     3's       ]  0	   [i)   full house  ]  0  \n" \
                   "[d)     4's       ]  0	   [j) small straight]  0               [total]  5\n" \
                   "[e)     5's       ]  0     [k) large straight]  0  \n" \
                   "[f)     6's       ]  0	   [l)    yahtzee    ]  0  \n" \
                   "[   upper bonus   ]  0     [m)    chance     ]  5    "
        actual = display_scoreboard(score=score)
        self.assertEqual(expected, actual)
