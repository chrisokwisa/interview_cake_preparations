# Write a function for reversing a linked list
# Your function will have one input: the head of the list
# Your function should return the new head of the list


import unittest


def reverse(head_of_list):

    # Reverse the linked list in place
    

    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current_node:
        # copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next

        # Reverse the 'next' pointer
        current_node.next = previous_node

        # step forward in the list
        previous_node = current_node
        current_node = next_node


    return previous_node



# Complexity
# O(n) time and O(1) space . We pass over the list only once, maintain
# a constant number of variables in memory


# Tests

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def test_short_linked_list(self):
        second = Test.LinkedListNode(2)
        first = Test.LinkedListNode(1, second)

        result = reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [2, 1]
        self.assertEqual(actual, expected)

    def test_long_linked_list(self):
        sixth = Test.LinkedListNode(6)
        fifth = Test.LinkedListNode(5, sixth)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)

        result = reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [6, 5, 4, 3, 2, 1]
        self.assertEqual(actual, expected)

    def test_one_element_linked_list(self):
        first = Test.LinkedListNode(1)

        result = reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [1]
        self.assertEqual(actual, expected)

    def test_empty_linked_list(self):
        result = reverse(None)
        self.assertIsNone(result)


unittest.main(verbosity=2)