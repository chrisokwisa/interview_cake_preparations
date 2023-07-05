# A building had 100 floors. One of the floors is the highest floor an egg can be dropped from without breaking.

# If an egg is dropped from above that floor, it will break. If it is dropped from that floor or below, 
# it will be completely undamaged and you can drop the egg again.

# Given two eggs, find the highest floor an egg can be dropped from without breaking, with as few drops as possible.

# Write a function that takes in a number of floors and returns the minimum number of drops needed to find the highest 
# floor an egg can be dropped from without breaking.

# For example, if the number of floors is 10, the function should return 4, because we 
# would want to drop the first egg at the 4th floor, the second egg at the 8th floor, and then the first egg again at the 10th floor.

# If the number of floors is 100, the function should return 14, because we would want to drop the first egg at the 14th floor, 
# the second egg at the 28th floor, and then the first egg again at the 56th floor, and so on.


# Complexity

# O(n) time and O(1) space.

# We iterate through the string once, and push and pop from the stack once. 
# Each of these operations is O(1)O(1), so the overall complexity is O(n)O(n).


# Tests

import unittest
import math

def egg_drop(floors):
    # Fill this in.

    # The first egg will be dropped from the first floor, the second egg from the second floor, and so on.
    # Determine the minimum number of drops required to guarantee success
    drops = math.ceil((-1 + math.sqrt(1 + 8*floors))/2)
    
    return drops


class Test(unittest.TestCase):

    def test_egg_drop(self):
        self.assertEqual(egg_drop(10), 4)
        self.assertEqual(egg_drop(100), 14)
   

if __name__ == '__main__':
    unittest.main()





