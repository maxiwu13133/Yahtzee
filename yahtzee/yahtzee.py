import random


def dice_art(dice_number: int) -> list:
    """Provide list of art for die roll numbers

    :param dice_number: an integer
    :precondition: integer must be in range(1, 7)
    :postcondition: fetch the list of die art for the chosen integer
    :return: a list
    >>> dice_art(4)
    ['o   o', '     ', 'o   o']
    >>> dice_art(3)
    ['    o', '  o  ', 'o    ']
    """

    if dice_number == 1:
        dice_picture = ['     ', '  o  ', '     ']
    elif dice_number == 2:
        dice_picture = ['    o', '     ', 'o    ']
    elif dice_number == 3:
        dice_picture = ['    o', '  o  ', 'o    ']
    elif dice_number == 4:
        dice_picture = ['o   o', '     ', 'o   o']
    elif dice_number == 5:
        dice_picture = ['o   o', '  o  ', 'o   o']
    else:
        dice_picture = ['o   o', 'o   o', 'o   o']
    return dice_picture


def dice_reformat(current_hand: list):
    """Convert current hand into art that looks like die

    :param current_hand: a list
    :precondition: list must have 5 indices in range(1, 7)
    :postcondition: have current hand look like die rolls and not numbers

    >>> dice_reformat([1, 2, 3, 4, 5])
    |     |    |    o|    |    o|    |o   o|    |o   o|
    |  o  |    |     |    |  o  |    |     |    |  o  |
    |     |    |o    |    |o    |    |o   o|    |o   o|
       1          2          3          4          5
    <BLANKLINE>
    >>> dice_reformat([6, 6, 6, 6, 6])
    |o   o|    |o   o|    |o   o|    |o   o|    |o   o|
    |o   o|    |o   o|    |o   o|    |o   o|    |o   o|
    |o   o|    |o   o|    |o   o|    |o   o|    |o   o|
       1          2          3          4          5
    <BLANKLINE>
    """
    dice_1 = dice_art(current_hand[0])
    dice_2 = dice_art(current_hand[1])
    dice_3 = dice_art(current_hand[2])
    dice_4 = dice_art(current_hand[3])
    dice_5 = dice_art(current_hand[4])
    hand = f'|{dice_1[0]}|    |{dice_2[0]}|    |{dice_3[0]}|    |{dice_4[0]}|    |{dice_5[0]}|\n' \
           f'|{dice_1[1]}|    |{dice_2[1]}|    |{dice_3[1]}|    |{dice_4[1]}|    |{dice_5[1]}|\n' \
           f'|{dice_1[2]}|    |{dice_2[2]}|    |{dice_3[2]}|    |{dice_4[2]}|    |{dice_5[2]}|\n' \
           f'   1          2          3          4          5\n'
    print(hand)


def roll_dice(current_hand: list, die_kept: str) -> list:
    """Roll the current player's hand

    :param current_hand: a list
    :precondition: list must be empty or have 5 indices in range(1, 7)
    :param die_kept: a string
    :precondition: string can not be more than 5 characters
    :precondition: string characters must be any of the following: 0 1 2 3 4 5
    :postcondition: rolls the current player's hand
    :return: a list
    """
    new_hand = random.choices(range(1, 7), k=5)
    if die_kept != '0':
        hand = list(die_kept)
        for index in hand:
            new_hand[int(index) - 1] = current_hand[int(index) - 1]
        return new_hand
    else:
        return new_hand


def category_checker(score: dict, target_category: str) -> bool:
    """Check if category already has a number value

    return True if no value else return False

    :param score: a dictionary
    :precondition: dictionary keys must be all 13 categories of Yahtzee
    :param target_category: a string
    :precondition: string must be a single letter that represents a choice from the list
    :postcondition: checks if player has already claimed the category
    :return: a boolean

    >>> category_checker({"1s": 2, "2s": 4, "3s": '', "4s": '', "5s": '', "6s": 12, "three": 15, \
                            "four": 22, "full": '', "small": 30, "large": 40, "yahtzee": 50, \
                            "chance": ''}, 'd')
    True
    >>> category_checker({"1s": 2, "2s": 4, "3s": 3, "4s": ' ', "5s": 15, "6s": 12, "three": 15, \
                            "four": 22, "full": 25, "small": 30, "large": 40, "yahtzee": 50, \
                            "chance": 11}, 'g')
    False
    """
    guide = {'a': '1s', 'b': '2s', 'c': '3s', 'd': '4s', 'e': '5s', 'f': '6s', 'g': 'three',
             'h': 'four', 'i': 'full', 'j': 'small', 'k': 'large', 'l': 'yahtzee', 'm': 'chance'}
    if target_category == 'l' and score['yahtzee'] != 0:
        return True
    elif score[guide[target_category]] != '':
        return False
    else:
        return True


def score_calculator(current_hand: list, target_category: str) -> int:
    """Calculate points for each category based on current hand

    :param current_hand: a list
    :precondition: list must have 5 indices in range(1, 7)
    :param target_category: a string
    :precondition: string must be a single letter that represents a choice from the list
    :postcondition: calculates points for the target category
    :return: an integer

    >>> score_calculator([2, 2, 3, 3, 3], 'i')
    25
    >>> score_calculator([1, 1, 1, 1, 1], 'l')
    50
    """
    upper_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    set_values_dict = {'i': 25, 'j': 30, 'k': 40, 'l': 50}
    points = 0

    if target_category in upper_dict.keys():
        for num in current_hand:
            if num == upper_dict[target_category]:
                points += num

    elif target_category in set_values_dict.keys():
        if hand_checker(current_hand, target_category):
            points += set_values_dict[target_category]

    else:
        if hand_checker(current_hand, target_category):
            for num in current_hand:
                points += num

    return points


def hand_checker(hand: list, category: str) -> bool:
    """Check if the hand qualifies for the category

    :param hand: a list
    :precondition: list must have 5 indices in range(1, 7)
    :param category: a string
    :precondition: string must be a single letter that represents a choice from the list
    :postcondition: verifies that the hand qualifies for the category
    :return: a boolean

    >>> hand_checker([2, 3, 4, 5, 5], 'k')
    False
    >>> hand_checker([2, 3, 4, 5, 5], 'j')
    True
    """
    hand_count_list = sorted([hand.count(1), hand.count(2), hand.count(3),
                              hand.count(4), hand.count(5), hand.count(6)])
    if category == 'g' and hand_count_list[-1] >= 3:
        return True
    elif category == 'h' and hand_count_list[-1] >= 4:
        return True
    elif category == 'i' and hand_count_list[-1] == 3 and hand_count_list[-2] == 2:
        return True
    elif category == 'j' and hand_count_list[2] == 1:
        return True
    elif category == 'k' and hand_count_list[1] == 1:
        return True
    elif category == 'l' and hand_count_list[-1] == 5:
        return True
    elif category == 'm':
        return True
    else:
        return False


def score_updater(score: dict, current_hand: list, target_category: str) -> dict:
    """Call score_calculator and update score dictionary

    :param score: a dictionary
    :precondition: dictionary keys must be all 13 categories of Yahtzee
    :param current_hand: a list
    :precondition: list must have 5 indices in range(1, 7)
    :param target_category: a string
    :precondition: string must be a single letter that represents a choice from the list
    :return: a dictionary

    >>> score_dict = {"1s": '', "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '', \
                      "four": '', "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''}
    >>> score_updater(score_dict, [1, 2, 3, 4, 5], 'd')
    {'1s': '', '2s': '', '3s': '', '4s': 4, '5s': '', '6s': '', 'three': '', 'four': '', \
'full': '', 'small': '', 'large': '', 'yahtzee': '', 'chance': ''}
    >>> score_dict = {"1s": '', "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '', \
                      "four": '', "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''}
    >>> score_updater(score_dict, [1, 2, 3, 4, 5], 'k')
    {'1s': '', '2s': '', '3s': '', '4s': '', '5s': '', '6s': '', 'three': '', 'four': '', \
'full': '', 'small': '', 'large': 40, 'yahtzee': '', 'chance': ''}
    """
    points = score_calculator(current_hand, target_category)
    guide = {'a': '1s', 'b': '2s', 'c': '3s', 'd': '4s', 'e': '5s', 'f': '6s', 'g': 'three',
             'h': 'four', 'i': 'full', 'j': 'small', 'k': 'large', 'l': 'yahtzee', 'm': 'chance'}
    if target_category == 'l' and score['yahtzee'] != '':
        score['yahtzee'] = score['yahtzee'] + 100
    else:
        score[guide[target_category]] = points
    return score


def display_scoreboard(score: dict):
    """Display current player's score

    :param score: a dictionary
    :precondition: dictionary keys must be all 13 categories of Yahtzee
    :postcondition: formats current score and prints it

    >>> display_scoreboard({"1s": 2, "2s": 4, "3s": 3, "4s": 8, "5s": 15, "6s": 12, "three": 15, \
                            "four": 22, "full": 25, "small": 30, "large": 40, "yahtzee": 50, \
                            "chance": 11})
    [a)     1's       ]  2  [g)Three of a kind]  15
    [b)     2's       ]  4  [h) four of a kind]  22
    [c)     3's       ]  3  [i)   full house  ]  25
    [d)     4's       ]  8  [j) small straight]  30 [total]  237
    [e)     5's       ]  15 [k) large straight]  40
    [f)     6's       ]  12 [l)    yahtzee    ]  50
    [   upper bonus   ]  0  [m)    chance     ]  11
    <BLANKLINE>
    >>> display_scoreboard({"1s": '', "2s": 2, "3s": 0, "4s": 4, "5s": 0, "6s": 6, "three": 15, \
                            "four": '', "full": 25, "small": '', "large": 40, "yahtzee": '', \
                            "chance": 11})
    [a)     1's       ]  	[g)Three of a kind]  15
    [b)     2's       ]  2	[h) four of a kind]
    [c)     3's       ]  0	[i)   full house  ]  25
    [d)     4's       ]  4	[j) small straight]  	[total]  103
    [e)     5's       ]  0	[k) large straight]  40
    [f)     6's       ]  6	[l)    yahtzee    ]
    [   upper bonus   ]  0	[m)    chance     ]  11
    <BLANKLINE>
    """
    display = f"[a)     1's       ]  {score['1s']}\t[g)Three of a kind]  {score['three']}\n" \
              f"[b)     2's       ]  {score['2s']}\t[h) four of a kind]  {score['four']}\n" \
              f"[c)     3's       ]  {score['3s']}\t[i)   full house  ]  {score['full']}\n" \
              f"[d)     4's       ]  {score['4s']}\t[j) small straight]  {score['small']}\t" \
              f"[total]  {total_calc(score)}\n" \
              f"[e)     5's       ]  {score['5s']}\t[k) large straight]  {score['large']}\n" \
              f"[f)     6's       ]  {score['6s']}\t[l)    yahtzee    ]  {score['yahtzee']}\n" \
              f"[   upper bonus   ]  {upper_calc(score)}\t[m)    chance     ]  {score['chance']}\n"
    print(display)


def upper_calc(score: dict) -> int:
    """Calculate if player has earned an upper bonus

    :param score: a dictionary
    :precondition: dictionary keys must be all 13 categories of Yahtzee
    :postcondition: calculates if current player has earned an upper bonus
    :return: an integer

    >>> upper_calc({"1s": '', "2s": 2, "3s": 0, "4s": 4, "5s": 0, "6s": 6, "three": 15, \
                    "four": '', "full": 25, "small": '', "large": 40, "yahtzee": '', "chance": 11})
    0
    >>> upper_calc({"1s": 4, "2s": 8, "3s": 12, "4s": 16, "5s": 15, "6s": 12, "three": 15, \
                    "four": '', "full": 25, "small": '', "large": 40, "yahtzee": '', "chance": 11})
    102
    """
    new_score = {'1s': score['1s'], '2s': score['2s'], '3s': score['3s'], '4s': score['4s'],
                 '5s': score['5s'], '6': score['6s']}
    upper_score = sum(num for num in new_score.values() if type(num) == int)
    if upper_score >= 63:
        return upper_score + 35
    else:
        return 0


def total_calc(score: dict) -> int:
    """Calculate the total score of the current player

    :param score: a dictionary
    :precondition: dictionary keys must be all 13 categories of Yahtzee
    :postcondition: calculates the total score of the current player
    :return: an integer

    >>> total_calc({"1s": '', "2s": 2, "3s": 0, "4s": 4, "5s": 0, "6s": 6, "three": 15, \
                    "four": '', "full": 25, "small": '', "large": 40, "yahtzee": '', "chance": 11})
    103
    >>> total_calc({"1s": 3, "2s": 6, "3s": 9, "4s": 12, "5s": 15, "6s": 18, "three": 20, \
                    "four": 20, "full": 25, "small": '', "large": 40, "yahtzee": '', "chance": 15})
    281
    """
    total = sum(num for num in score.values() if type(num) == int)
    total += upper_calc(score)
    return total


def game_results(score: dict):
    """Determine winner of Yahtzee

    :param score: a list
    :precondition: list of 2 dictionaries with keys being all 13 categories of Yahtzee
    :postcondition: takes into account total points and determines winner
    :return: a string

    >>> game_results({0: {"1s": 2, "2s": 4, "3s": 3, "4s": 8, "5s": 15, "6s": 12, "three": 15, \
"four": 22, "full": 25, "small": 30, "large": 40, "yahtzee": 50, "chance": 11}, 1: {"1s": 1, \
"2s": 0, "3s": 3, "4s": 0, "5s": 0, "6s": 6, "three": 0, "four": 23, "full": 25, \
"small": 30, "large": 0, "yahtzee": 0, "chance": 25}})
    'Score is 237:113'
    'Player 1 wins!'
    >>> game_results({0: {"1s": 0, "2s": 4, "3s": 0, "4s": 8, "5s": 5, "6s": 12, "three": 15, \
    "four": 22, "full": 25, "small": 0, "large": 40, "yahtzee": 0, "chance": 11}, 1: {"1s": 0, \
    "2s": 4, "3s": 0, "4s": 8, "5s": 5, "6s": 12, "three": 15, "four": 22, "full": 25, "small": 0, \
    "large": 40, "yahtzee": 0, "chance": 11}})
    'Score is 142:142'
    'Tie!'
    """
    player_one_total = total_calc(score[0])
    player_two_total = total_calc(score[1])

    if player_one_total > player_two_total:
        print(f'Score:\nPlayer 1: {player_one_total}\nPlayer 2: '
              f'{player_two_total}\n\nPlayer 1 wins!')
    if player_one_total < player_two_total:
        print(f'Score:\nPlayer 1: {player_one_total}\nPlayer 2: '
              f'{player_two_total}\n\nPlayer 2 wins!')
    else:
        print(f'Score:\nPlayer 1: {player_one_total}\nPlayer 2: {player_two_total}\n\nTie!')


def player_turn(score: dict, player: int) -> int:
    """Alternate scoreboards for player 1 and 2

    :param score: a dictionary
    :precondition: dictionary of 2 dictionaries, sub dictionary must have all 13 categories
    :param player: an integer
    :precondition: an integer of 1 or 2
    :postcondition: alternates between player 1 and 2
    :return: an integer

    >>> player_turn({0: {"1s": '', "2s": 4, "3s": 0, "4s": 8, "5s": 5, "6s": 12, "three": 15, \
    "four": 22, "full": '', "small": 0, "large": '', "yahtzee": 0, "chance": 11}, 1: {"1s": 0, \
    "2s": 4, "3s": 0, "4s": 8, "5s": 5, "6s": 12, "three": 15, "four": 22, "full": 25, "small": 0, \
    "large": 40, "yahtzee": 0, "chance": 11}}, 1)
    0
    >>> player_turn({0: {"1s": '', "2s": 4, "3s": 0, "4s": 8, "5s": 5, "6s": 12, "three": 15, \
    "four": 22, "full": '', "small": 0, "large": '', "yahtzee": 0, "chance": 11}, 1: {"1s": 0, \
    "2s": 4, "3s": 0, "4s": 8, "5s": 5, "6s": 12, "three": 15, "four": 22, "full": 25, "small": 0, \
    "large": 40, "yahtzee": 0, "chance": 11}}, 0)
    0
    """
    counter_one = 0
    counter_two = 0

    for values in score[0].values():
        if values != '':
            counter_one += 1

    for values in score[1].values():
        if values != '':
            counter_two += 1

    if counter_one < 13 and counter_two < 13 and player == 0:
        return 1
    elif counter_one < 13 and counter_two < 13 and player == 1:
        return 0
    elif counter_one == 13 and counter_two < 13:
        return 1
    elif counter_two == 13 and counter_one < 13:
        return 0
    else:
        return 2


def STARTER_PACK():
    """
    Variables to start the game
    """
    score = {0: {"1s": '', "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '',
                 "four": '', "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''},
             1: {"1s": '', "2s": '', "3s": '', "4s": '', "5s": '', "6s": '', "three": '',
                 "four": '', "full": '', "small": '', "large": '', "yahtzee": '', "chance": ''}}
    hand = random.choices(range(1, 7), k=5)
    roll_counter = 0
    player = 0
    return score, hand, roll_counter, player


def RULES():
    """
    Print rules to the game
    """
    print('Welcome to my Yahtzee game!\n'
          '\n'
          '1. To roll your hand again, enter 0\n'
          '\n'
          '2. To choose die to keep, enter the corresponding numbers beneath the die\n'
          '   e.g., 134 to keep the 1st, 3rd and 4th die. Order of the numbers do not matter\n'
          '\n'
          '3. You only have 2 rerolls, any more after that will not affect the hand\n'
          '\n'
          '4. Enter a letter to score your current hand into the corresponding category\n'
          '   and pass the turn over to your opponent\n'
          '\n'
          'If you enter anything other than what I specified, the outcome is on you :)')


def menu():
    """Ask user for input and call helper functions accordingly

    :postcondition: continuously asks user for inputs
    """
    RULES()
    score, hand, roll_counter, player = STARTER_PACK()
    while player == 1 or player == 0:
        print(f"\nPlayer {player + 1}")
        dice_reformat(hand)
        display_scoreboard(score[player])
        if roll_counter == 2:
            print('You have no more rolls')
        user_choice = input('Enter a move:\n')
        if user_choice.isdigit() and roll_counter != 2:
            hand = roll_dice(hand, str(user_choice))
            roll_counter += 1
        elif user_choice.isalpha() and category_checker(score[player], user_choice):
            score[player] = score_updater(score[player], hand, user_choice)
            roll_counter = 0
            hand = random.choices(range(1, 7), k=5)
            player = player_turn(score, player)
    game_results(score)
    quit()


def main():
    """
    Execute the program
    """
    import doctest
    doctest.testmod()
    # menu()


if __name__ == '__main__':
    main()
