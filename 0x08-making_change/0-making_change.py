#!/usr/bin/python3
"""Module for Making Change.
"""


def makeChange(coins, total):
    """Calculates the fewest number of coins needed to meet a given total.

    If total is 0 or less, returns 0. If total cannot be met by any number
    of coins, returns -1.
    Assumes that coins is a list of the values of the coins in your
    possession, the value of a coin is always an integer greater than 0,
    and you have an infinite number of each denomination of coin.

    Args:
        coins (list[int]): A list of coin values.
        total (int): The total amount of money to make.

    Returns:
        int: The fewest number of coins needed to meet the total.
    """
    # If the total is zero or less, we don't need any coins
    if total <= 0:
        return 0
    # Sort the coins in decreasing order
    coins.sort(reverse=True)
    # Initialize the coin count to zero
    coin_count = 0
    # Iterate through each coin in the list of coins
    for coin in coins:
        # If the coin is greater than the remaining total, skip it
        if coin > total:
            continue
        # Calculate the number of times the current coin can be used
        count = total // coin
        # Update the total by subtracting the value of the coins used
        total -= count * coin
        # Update the coin count by adding the number of coins used
        coin_count += count
        # If the total is now zero, we're done
        if total == 0:
            break
    # If we couldn't make change for the total, return -1
    if total > 0:
        return -1
    # Otherwise, return the coin count
    return coin_count
