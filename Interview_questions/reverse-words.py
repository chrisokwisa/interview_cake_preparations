# Write a function reverse_words() that takes a message as a list
#  of characters and reverses the order of the words in place

import unittest

def reverse_words(message):
    # First we reverse all the characters in the entite message
    reverse_characters(message, 0, len(message)-1)

    # This gives us the right word order
    # but with each word backward

    # We hold the index of the 'start' of the current word
    


def reverse_characters(message, left_index, right_index):
    #  Walk towards the middle, from both sides

    left_index  = 0
    right_index = len(message) - 1

    while left_index < right_index:
        # swap characters
        message[left_index], message[right_index] = \
        message[right_index], message[left_index]

        #  Move towards middle
        left_index += 1
        right_index += 1

# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)