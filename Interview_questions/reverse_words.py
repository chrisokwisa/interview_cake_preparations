# Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place

# Why a list of characters instead of a string?

# What is a list of characters?


# What is a string?

# What is a list?  

# The goal of this question is to practice manipulating strings in place. Since we're modifying the input, we need a mutable type like a list, instead of Python's immutable strings.

# mutable object can be changed after it's created and an immutable object can't

# for example

# lists are mutable in python

# int_list = [1,2,3,4,5]
# int_list[0] = 10
# print(int_list)

# output
# [10, 2, 3, 4, 5]

# strings are immutable in python

# string = "hello"
# string[0] = "H"
# print(string)

# output
# TypeError: 'str' object does not support item assignment

# Solution

import unittest

# def reverse_words(message):
    
        # Decode the message by reversing the words
        # for example
        # input = ['c', 'a', 'k', 'e', ' ',
        #          'p', 'o', 'u', 'n', 'd', ' ',
        #          's', 't', 'e', 'a', 'l']
        # output = ['s', 't', 'e', 'a', 'l',
        #           ' ',
        #           'p', 'o', 'u', 'n', 'd',
        #           ' ',
        #           'c', 'a', 'k', 'e']
    
        # we can use the reverse function from reverse_string to reverse the entire message
        # then we can use the reverse_words function from reverse_words to reverse the words in the message

        # reverse the entire message
        # reverse the words in the message

        # we can use a two pointer approach to do this
        # one pointer at the start of the word and one at the end of the word

        # we can use a while loop to do this
        # while left < right



def reverse_words(message):
    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, len(message)-1)

    # This gives us the right word order
    # but with each word backward

    # Now we'll make the words forward again
    # by reversing each word's characters

    # We hold the index of the *start* of the current word
    # as we look for the *end* of the current word
    current_word_start_index = 0

    for i in range(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            # If we haven't exhausted the message our
            # next word's start is one character ahead
            current_word_start_index = i + 1


def reverse_characters(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index  += 1
        right_index -= 1


# complexity 
# O(n) time and O(1) space

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
        message = list('get another one')
        reverse_words(message)
        expected = list('one another get')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('yummy is a cake bundy chocolate')
        reverse_words(message)
        expected = list('chocolate bundy cake a is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)

unittest.main(verbosity=2)



