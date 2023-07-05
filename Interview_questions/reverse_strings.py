# Write a function that takes a list characters and reverses the letters in place

# Why a list of chracters instead of a string?

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

def reverse(list_of_chars):
    
        # Reverse the input list of chars in place
        # for example
        # input = ['h', 'e', 'l', 'l', 'o']
        # output = ['o', 'l', 'l', 'e', 'h']
        
        # we can use two pointer approach to solve this problem
        # one pointer at the start and one at the end
        # swap the values at the pointers and move the pointers towards the middle
        # when the pointers meet we are done
        
        # we can use a while loop to do this
        # while left < right
        # swap the values at the pointers
        # move the pointers towards the middle
        
        left = 0
        right = len(list_of_chars) - 1
        
        while left < right:
            # swap the values at the pointers
            # we can use tuple unpacking to do this
            # we can also use a temp variable to do this
            list_of_chars[left], list_of_chars[right] = list_of_chars[right], list_of_chars[left]
            # move the pointers towards the middle
            left += 1
            # we can also use left = left + 1
            # we can also use left += 1
            # we can also use left++
            right -= 1

# Complexity
# O(n) time and O(1) space

# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        actual = list_of_chars
        self.assertEqual(actual, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        actual = list_of_chars
        self.assertEqual(actual, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        actual = list_of_chars
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)

# output
# python reverse_strings.py
# test_empty_string (__main__.Test) ... ok
# test_longer_string (__main__.Test) ... ok
# test_single_character_string (__main__.Test) ... ok




