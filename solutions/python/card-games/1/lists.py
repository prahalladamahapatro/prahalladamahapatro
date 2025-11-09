"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    #l = []
    #l.extend([number, number + 1, number + 2])
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return True if number in rounds else False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    return True if (sum(hand) / len(hand) == (hand[0] + hand[-1]) / 2) or (sum(hand) / len(hand) == hand[len(hand)//2]) else False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    #Things to remember:
    # 1. Inside the LOOP, always use an IF-ELSE statement. Don't skip the ELSE part, like in the return statement; otherwise, you'll get all values from the original list to the l2 list.
    # 2. Don't use APPEND, 
    l1 = l2 = []
    for i in range(0,len(hand)):
        if i % 2 == 0:
            l1 = l1 + [hand[i]]
        else:    
            l2 = l2 + [hand[i]]
    return True if sum(l1)/len(l1) == sum(l2)/len(l2) else False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand.pop()
        return hand + [22]
    return hand
        
        
    
