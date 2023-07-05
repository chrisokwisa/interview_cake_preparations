# Write an efficient function that takes stock_prices 
# and returns the best profit I could have made from one purchase and one sale of
# one share of Apple Stock yesterday


# Example:
# stock_prices = [10, 7, 5, 8, 11, 9]
# get_max_profit(stock_prices)
# returns 6 (buying for $5 and selling for $11)

# No "shorting" - you need to buy before you can sell
# You can't buy and sell in the same time step - at least 1 minute has to pass


# Brute force solution
# O(n^2) time
# O(1) space
# def get_max_profit(stock_prices):
#     max_profit = stock_prices[1] - stock_prices[0]

#     for earlier_time, earlier_price in enumerate(stock_prices):
#         for later_price in stock_prices[earlier_time + 1:]:
#             potential_profit = later_price - earlier_price
#             max_profit = max(max_profit, potential_profit)

#     return max_profit

# Greedy solution
# O(n) time
# O(1) space
def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]


    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # this would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.

    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit

# Path: Interview_questions\apple_stokes.py
# Compare this snippet from Interview_questions\reverse-words.py:
# # Write a function reverse_words() that takes a message as a list

#  of characters and reverses the order of the words in place





# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_big_increase_then_small_increase(self):
        actual = get_max_profit([2, 10, 1, 4])
        expected = 8
        self.assertEqual(actual, expected)                

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)