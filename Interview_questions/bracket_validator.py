# Write a function that tells whether an input string's openers and closers are properly nested.

# For example, "{ [ ] ( ) }" should return True. "{ [ ( ] ) }" should return False.

# We can assume the input string only contains openers and closers, and openers and closers of the same type.

# As a bonus, return the position of the first offending closer if the string is not properly nested.   

# If the string is properly nested, return 1.

# If the string is not properly nested, return the position of the first offending closer.

# Examples:

# "{ [ ] ( ) }" should return 1

# "{ [ ( ] ) }" should return 7

# "{ [ }" should return 3

# Complexity

# O(n) time and O(n) space.

# We iterate through the string once, and push and pop from the stack once. Each of these operations is O(1)O(1), so the overall complexity is O(n)O(n).

# Tests

import unittest

def is_valid(code):
    
        # Determine if the input code is valid
    
        openers_to_closers = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
    
        openers = set(openers_to_closers.keys())
        closers = set(openers_to_closers.values())
    
        openers_stack = []
    
        for i, char in enumerate(code):
    
            if char in openers:
                openers_stack.append(char)
    
            elif char in closers:
    
                if not openers_stack:
                    return i
    
                else:
                    last_unclosed_opener = openers_stack.pop()
    
                    # If this closer doesn't correspond to the most recently
                    # seen unclosed opener, short-circuit, returning false
                    if not openers_to_closers[last_unclosed_opener] == char:
                        return i
    
        return 1 if not openers_stack else len(code)



class Test(unittest.TestCase):
     
    def test_valid_short_code(self):
        actual = is_valid('()')
        expected = 1
        self.assertEqual(actual, expected)

    def test_mismatched_opener_and_closer(self):
        actual = is_valid('([]{[])}')
        expected = 7
        self.assertEqual(actual, expected)

    def test_missing_closer(self):
        actual = is_valid('[[]()')
        expected = 5
        self.assertEqual(actual, expected)

    def test_extra_closer(self):
        actual = is_valid('[[]]())')
        expected = 6
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        actual = is_valid('')
        expected = 1
        self.assertEqual(actual, expected)

    

unittest.main(verbosity=2)

# Path: Interview_questions\bracket_validator.py