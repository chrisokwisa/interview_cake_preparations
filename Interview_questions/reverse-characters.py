
#  Write a function that takes a list characters and reverses the letters in place


# swap the first and last characters, then the second and second-to-last
# characters, and so on until we reach the middle

import unittest

def reverse(list_of_chars):

    left_index = 0 # because we want to start at the beginning
    right_index = len(list_of_chars) - 1 # because we want to start at the end

    while left_index < right_index:
        # swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
        list_of_chars[right_index], list_of_chars[left_index]

        #  Move towards middle
        left_index += 1 # 
        right_index -= 1



        # complexity
        #  O(n) and O(1) space





# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)